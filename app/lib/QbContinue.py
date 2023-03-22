import os
from lib.XLog import XLog
from lib.XQBittorrent import XQBittorrentApi
from lib.XTorrent import XTorrent


# 递归获取所有文件
def get_all_files(path):
    files = []
    os.chdir(path)
    file_list = os.listdir()
    for file in file_list:
        file_path = os.path.join(path, file)
        files.append(file_path)
        if os.path.isdir(file_path):
            try:
                files.extend(get_all_files(file_path))
            except PermissionError:
                pass
    return files


# 获取第一层文件夹所有文件
def get_first_dir_files(path):
    files = []
    os.chdir(path)
    file_list = os.listdir()
    for file in file_list:
        file_path = os.path.join(path, file)
        files.append(file_path)
    return files


if __name__ == '__main__':
    from config import qbtorrentcfg

    logger = XLog()
    logger.info("------------------开始运行------------------")
    torrent_path = qbtorrentcfg["torrent_path"]
    search_path = qbtorrentcfg["search_path"]
    torrents = os.listdir(torrent_path)
    path_list = get_first_dir_files(search_path)

    qbtorrent = XQBittorrentApi(qbtorrentcfg["host"], qbtorrentcfg["username"], qbtorrentcfg["password"],
                                qbtorrentcfg["tag"])

    for torrent in torrents:
        if not os.path.isdir(torrent) and torrent.endswith('torrent'):
            torrens_file = os.path.join(torrent_path, torrent)
            x_torrent = XTorrent(torrens_file)
            filename = x_torrent.get_path_name()
            torrent_hash = x_torrent.get_hash()
            for path in path_list:
                path_name = path.split('\\')[-1]
                if filename == path_name:
                    try:
                        save_path = '\\'.join(path.split('\\')[:-1])
                        qbtorrent.add_torrent_to_run(torrens_file, save_path=save_path)
                        qbtorrent.add_tag_to_torrent(torrent_hash)
                        logger.info(f"成功添加 {torrens_file}")
                    except Exception as e:
                        logger.error(f"{torrent} 任务已存在")
    logger.info("------------------运行结束------------------")
