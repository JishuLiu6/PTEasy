from synology_api import filestation, downloadstation


class XSynologyApi:
    '''
    Synology API: https://github.com/N4S4/synology-api
    '''
    def __init__(self, host, port, username, password, version=7):
        self.client = filestation.FileStation(host, port, username, password, secure=False, cert_verify=False,
                                              dsm_version=version, debug=True, otp_code=None)

    def get_file_list(self, path):
        return self.client.get_file_list(path)

    def get_file_info(self, path):
        return self.client.get_file_info(path)


if __name__ == '__main__':
    synology_bot = XSynologyApi('192.168.195.100', '5000', 'jishuliu620', 'Lzw990620')
    print(synology_bot.get_file_info('/docker'))