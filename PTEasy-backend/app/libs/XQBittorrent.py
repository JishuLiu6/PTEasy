from qbittorrentapi import Client


class XQBittorrentApi:
    def __init__(self, host, username, password, tag_name):
        self.client = Client(host=host, username=username, password=password)
        self.tag_name = tag_name

    def torrents_list(self) -> None:
        for torrent in self.client.torrents_info():
            data = {
                '种子名': torrent.name,
                '状态': torrent.state,
                'hash': torrent.hash,
                '正在下载数': torrent['num_leechs'],
                '完成下载数': torrent['num_complete'],
                '种子连接数': torrent['num_incomplete']
            }
            yield data


    def add_tag_to_torrent(self, torrent_hash, **kwargs):
        self.client.torrents_addTags(tags=self.tag_name, torrent_hashes=torrent_hash, **kwargs)

    def add_torrent_to_run(self, torrent_path, **kwargs):
        self.client.torrents_add(torrent_files=open(torrent_path, 'rb'), **kwargs)

    def pause_torrent(self, torrent_hash, **kwargs):
        self.client.torrents_pause(torrent_hashes=torrent_hash, **kwargs)

    def delete_torrent(self, torrent_hash, delete_files=False, **kwargs):
        self.client.torrents_delete(delete_files=delete_files, torrent_hashes=torrent_hash, **kwargs)


if __name__ == '__main__':
    qb_bot = XQBittorrentApi()
    print(qb_bot.show_torrents_list())
    # qb_bot.add_torrent_to_run('./PtData/')
