import hashlib
from bencoding import bencode, bdecode


class XTorrent:
    def __init__(self, filename):
        torrent_file = open(filename, "rb")
        self.decoded_dict = bdecode(torrent_file.read())

    def get_hash(self) -> str:
        torrent_hash = hashlib.sha1(bencode(self.decoded_dict[b"info"])).hexdigest()
        return torrent_hash

    def get_path_name(self) -> str:
        return self.decoded_dict[b'info'][b'name'].decode()


if __name__ == '__main__':
    torrent_path = 'E:\EdgeDownload\[M-TEAM]苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇.torrent'
    print(XTorrent(torrent_path).get_hash())
    print(XTorrent(torrent_path).get_path_name())
