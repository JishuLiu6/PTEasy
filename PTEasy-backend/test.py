from synology_api import filestation, downloadstation

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password) 
# it will log in automatically #
# NOTE: for Filestation and Downloadstation only has been added interactive_output=True, #
# It can be omitted and initiate the wrapper with the below ove code  
# fl = filestation.FileStation('Synology Ip', 'Synology Port', 'Username', 'Password', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
fl = filestation.FileStation('192.168.195.100', '5000', 'jishuliu620', 'Lzw990620', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
print(fl.get_file_list('/docker'))
print(fl.get_file_info('/docker'))
