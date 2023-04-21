import mimetypes
import os
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

from app.libs.task_handler import TaskHandler


def get_size(path) -> int:
    '''
    获取目录或文件的大小
    :param path:
    :return: t_size
    '''

    if os.path.isfile(path):
        t_size = os.path.getsize(path)
    elif os.path.isdir(path):
        t_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                try:
                    t_size += os.path.getsize(os.path.join(dirpath, filename))
                except FileNotFoundError:
                    continue
                except PermissionError:
                    continue
    else:
        t_size = 0
    return t_size


def get_file_info(file_entry, task) -> None:
    '''
    获取目录或文件的大小
    :param file_entry:
    :param task:
    :return: t_size
    '''
    task.step_start(file_entry['path'])
    try:
        sub_filepath_info = file_entry['stat']
        if file_entry['is_file']:
            # file_type = "file"
            file_type = get_file_type(file_entry['path'])
            file_size = sub_filepath_info.st_size
        else:
            file_type = "dir"
            file_size = get_size(file_entry['path'])

        if file_size != 0:
            atime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_atime))
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_filepath_info.st_mtime))

            from app.models.FileInfo import FileInfo
            FileInfo.create({'soft_path': file_entry['path'],
                             'file_name': os.path.basename(file_entry['path']),
                             'file_size': file_size,
                             'file_type': file_type,
                             'visit_time': atime,
                             'modify_time': mtime,
                             'file_id': sub_filepath_info.st_ino,
                             'parent_id': os.stat(os.path.dirname(file_entry['path'])).st_ino})
            # 发送步骤完成
            task.step_completed(file_entry['path'])
    except Exception as e:
        # 发送步骤错误
        task.step_error(file_entry)

        return None


def file_task(real_path, taskid) -> None:
    '''
    文件任务
    :param real_path: 文件路径
    :param taskid: 任务id
    '''
    try:
        task = TaskHandler(task_id=taskid, task_type='扫描目录')
        with os.scandir(real_path) as entries:
            entries_list = list(entries)
            total_entries = len(entries_list)
            # socket发送任务长度消息
            task.start_task(total_entries)
            for entry in entries_list:
                # 为了序列化记录，这里需要将entry转换为dict
                entry_dict = {
                    'stat': entry.stat(),
                    'is_file': entry.is_file(),
                    'path': entry.path
                }
                with ThreadPoolExecutor() as executor:
                    executor.map(lambda x: get_file_info(entry_dict, task), [None])
    except FileNotFoundError:
        task.step_error(f'{real_path} 目录不存在')
        return None


def get_file_type(file_path) -> str:
    '''
    获取文件类型
    '''
    mime_type, _ = mimetypes.guess_type(file_path)
    file_extension = os.path.splitext(file_path)[1]
    # print(file_extension)
    script_extensions = [
        '.py', '.js', '.sh', '.rb', '.php', '.java', '.c', '.cpp', '.cs', '.go',
        '.scala', '.rs', '.swift', '.kt', '.hs', '.f', '.erl', '.r', '.pl', '.m',
        '.lua', '.groovy', '.coffee', '.ts'
    ]

    if not mime_type and file_extension not in script_extensions:
        return 'other'

    mime_prefix_mapping = {
        'video': 'video',
        'image': 'image',
        'audio': 'audio',
    }

    for prefix, file_type in mime_prefix_mapping.items():
        if mime_type and mime_type.startswith(prefix):
            return file_type

    document_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.oasis.opendocument.text',
        'application/vnd.ms-powerpoint',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/vnd.oasis.opendocument.presentation'
    ]

    spreadsheet_types = [
        'application/vnd.ms-excel',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.oasis.opendocument.spreadsheet',
        'text/csv'
    ]

    application_types = [
        'application/x-msdownload',
        'application/vnd.android.package-archive',
        'application/x-executable',
        'application/x-dosexec',
        'application/java-archive',
        'application/x-apple-diskimage',
        'application/octet-stream'
    ]

    if file_extension in script_extensions:
        return 'script'
    elif any(mime_type.startswith(doc_type) for doc_type in document_types):
        return 'document'
    elif any(mime_type.startswith(sheet_type) for sheet_type in spreadsheet_types):
        return 'spreadsheet'
    elif any(mime_type.startswith(app_type) for app_type in application_types):
        return 'application'
    elif mime_type.startswith('text'):
        return 'text'
    else:
        return 'other'


if __name__ == '__main__':
    test_cases = {
        "test": "other",
        "sample.jpg": "image",
        "sample.mp4": "video",
        "sample.txt": "text",
        "sample.pdf": "document",
        "sample.xlsx": "spreadsheet",
        "sample.exe": "application",
        "sample.py": "script",
        "sample.js": "script",
        "sample.unknown": "other",
        "sample.mp3": "audio",
        "sample.docx": "document",
        "sample.csv": "spreadsheet",
        "sample.jar": "application",
        "sample.sh": "script",
        "sample.rb": "script",
        "sample.php": "script",
        "sample.java": "script",
        "sample.c": "script",
        "sample.cpp": "script",
        "sample.cs": "script",
        "sample.go": "script",
        "sample.scala": "script",
        "sample.rs": "script",
        "sample.swift": "script",
        "sample.kt": "script",
        "sample.hs": "script",
        "sample.f": "script",
        "sample.erl": "script",
    }

    for file_name, expected_type in test_cases.items():
        try:
            detected_type = get_file_type(file_name)
            assert detected_type == expected_type, f"{file_name}: expected {expected_type}, got {detected_type}"
            print(f"{file_name}: {detected_type}")
        except AssertionError as e:
            print(e)
