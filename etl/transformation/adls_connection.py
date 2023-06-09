# Import libraries
import io
import requests
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions, BlobServiceClient

# Set up Azure Datalake Storage
account_name = 'adlsglobantpoc'
account_key = 'bre+fddIXPLfnpixCAA07xE98e0ssIxSqNE2kuVh/mxTzILFcePtz72CR6iK8bhD/Z4AhVo+ioND+AStZWhDHQ=='
container_name = 'poc'

# Setting connection string
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'

# Create function reading files on adls
def read_file_adls(directory, file_name):
    # directory is the path on adls where we'll find files request
    # file_name is the file that we'll read
    
    sas = generate_blob_sas(account_name = account_name,
                          container_name = container_name,
                          blob_name = directory + '/' + file_name,
                          account_key = account_key,
                          permission = BlobSasPermissions(read=True),
                          expiry = datetime.utcnow() + timedelta(hours=24))
    path_adls = 'https://' + account_name + '.blob.core.windows.net/' + container_name + '/' + directory + '/' + file_name + '?' + sas
    path_adls_text = requests.get(path_adls).text
    path_adls_io = io.StringIO(path_adls_text)

    return path_adls_io

def upload_file_adls(file_path, directory):
    blob_services = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_services.get_blob_client(container=container_name, blob=directory)
    if blob_client.exists():
        blob_client.delete_blob()
    else:
        with open(file_path, 'rb') as data:
            blob_client.upload_blob(data)
    print(f"upload {directory}")