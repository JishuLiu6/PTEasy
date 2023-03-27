from synology_api import filestation, downloadstation

fl = filestation.FileStation('192.168.195.100', '5000', 'jishuliu620', 'Lzw990620', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
print(fl.get_file_list('/'))
# print(fl.get_file_info('/docker'))
