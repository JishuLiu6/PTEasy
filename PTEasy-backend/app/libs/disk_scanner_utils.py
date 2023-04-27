import asyncio
import mimetypes
import os
import time
from app.libs.task_helper import TaskHandler, LogLevel
from typing import List, Dict

SCRIPT_EXTENSIONS = [
    '.py', '.js', '.sh', '.rb', '.php', '.java', '.c', '.cpp', '.cs', '.go',
    '.scala', '.rs', '.swift', '.kt', '.hs', '.f', '.erl', '.r', '.pl', '.m',
    '.lua', '.groovy', '.coffee', '.ts'
]

DOCUMENT_TYPES = [
    'application/pdf',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.oasis.opendocument.text',
    'application/vnd.ms-powerpoint',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'application/vnd.oasis.opendocument.presentation'
]

SPREADSHEET_TYPES = [
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.oasis.opendocument.spreadsheet',
    'text/csv'
]

APPLICATION_TYPES = [
    'application/x-msdownload',
    'application/vnd.android.package-archive',
    'application/x-executable',
    'application/x-dosexec',
    'application/java-archive',
    'application/x-apple-diskimage',
    'application/octet-stream'
]

MIME_PREFIX_MAPPING = {
    'video': 'video',
    'image': 'image',
    'audio': 'audio',
}


async def get_size(path, task) -> int:
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                try:
                    filepath = os.path.join(dirpath, filename)
                    filesize = os.path.getsize(filepath)
                    total_size += filesize
                except FileNotFoundError:
                    continue
                except PermissionError:
                    await task.step(LogLevel.WARNING, f'{filepath} 文件夹没有权限')
                    continue
    else:
        total_size = 0
    return total_size


async def get_file_info(file_entry, task) -> None:
    await task.step(LogLevel.INFO, f'开始处理 {file_entry["path"]}')
    try:
        sub_filepath_info = file_entry['stat']
        if file_entry['is_file']:
            file_type = get_file_type(file_entry['path'])
            file_size = os.path.getsize(file_entry['path'])
        else:
            file_type = "dir"
            file_size = await get_size(file_entry['path'], task)

        # atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_atime))
        # mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_mtime))

        from app.models.FileInfo import FileInfo
        FileInfo.create({'soft_path': file_entry['path'],
                         'file_name': os.path.basename(file_entry['path']),
                         'file_size': file_size,
                         'file_type': file_type,
                         'visit_time': sub_filepath_info.st_atime,
                         'modify_time': sub_filepath_info.st_mtime,
                         'file_id': sub_filepath_info.st_ino,
                         'parent_id': os.stat(os.path.dirname(file_entry['path'])).st_ino})
        await task.step(LogLevel.SUCCESS, f'处理 {file_entry["path"]} 完成')
    except FileNotFoundError:
        await task.step(LogLevel.ERROR, f'{file_entry["path"]} 文件不存在')
        return None
    except Exception as e:
        await task.step(LogLevel.ERROR, f'在处理 {file_entry["path"]} 时发生错误: {str(e)}')
        return None


async def file_task(real_path, taskid, websocket=None, concurrency_limit=5) -> None:
    try:
        task = TaskHandler(task_id=taskid, task_type='扫描目录', task_name=real_path, websocket=websocket)
        with os.scandir(real_path) as entries:
            entries_list = list(entries)
            total_entries = len(entries_list)

            await task.step(LogLevel.SUCCESS, f'扫描到 {total_entries} 个文件, 开始任务', task_len=total_entries)

            # 使用信号量限制并发数
            sem = asyncio.Semaphore(concurrency_limit)

            async def process_entry(entry):
                async with sem:
                    entry_dict = {
                        'stat': entry.stat(),
                        'is_file': entry.is_file(),
                        'path': entry.path
                    }
                    await get_file_info(entry_dict, task)

            await asyncio.gather(*(process_entry(entry) for entry in entries_list))

    except FileNotFoundError:
        await task.step(LogLevel.ERROR, f'{real_path} 目录不存在')
        return None
    except Exception as e:
        await task.step(LogLevel.ERROR, f'在处理 {real_path} 时发生错误: {str(e)}')
        return None


def get_file_type(file_path) -> str:
    mime_type, _ = mimetypes.guess_type(file_path)
    file_extension = os.path.splitext(file_path)[1]

    if not mime_type and file_extension not in SCRIPT_EXTENSIONS:
        return 'other'

    for prefix, file_type in MIME_PREFIX_MAPPING.items():
        if mime_type and mime_type.startswith(prefix):
            return file_type

    if any(mime_type.startswith(doc_type) for doc_type in DOCUMENT_TYPES):
        return 'document'
    elif any(mime_type.startswith(sheet_type) for sheet_type in SPREADSHEET_TYPES):
        return 'spreadsheet'
    elif any(mime_type.startswith(app_type) for app_type in APPLICATION_TYPES):
        return 'application'
    elif mime_type.startswith('text'):
        return 'text'
    elif file_extension in SCRIPT_EXTENSIONS:
        return 'script'
    else:
        return 'other'


if __name__ == '__main__':
    import uuid

    taskid = str(uuid.uuid4())
    real_path = '/Users/jishuliu/Desktop'
    concurrency_limit = 10
    asyncio.run(file_task(real_path, taskid, None, concurrency_limit))