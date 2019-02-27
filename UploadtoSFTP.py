import os
import pysftp
import time
import paramiko


# https://stackoverflow.com/questions/43357295/looking-for-an-example-to-load-use-a-public-ssh-key-with-pysftp
def sftp_upload(edi_file):
    host = "s-8cfcba85595d4d749.server.transfer.us-east-1.amazonaws.com"
    user_name = "springdealerworkspaceuser"
    pk_file = paramiko.AgentKey.from_private_key_file(filename="private_key", password=str(None))

    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        # Define the actual SFTP connection
        with pysftp.Connection(host=host, port=22, username=user_name, private_key=pk_file, cnopts=cnopts) as sftp:
            sftp.put(edi_file)
            # once the upload is done return a success message
            # at this point return or send an email to stake holders that
            # the file is uploaded to SFTP
            return 'ATT Dashboard Metrics file {} has been uploaded successfully'.format(edi_file)
    except(IOError, OSError):

        return 'Att Dashboard Metrics file {} failed to upload'.format(edi_file)


my_path = 'C:/Downloads/AttDashboard/'
for item in os.listdir(my_path):  # loop through items in dir
    if item.endswith('.dat'):
        file_path = os.path.join(my_path, item)
        sftp_upload(file_path)
        time.sleep(40)
    break
