import datetime
import os
import subprocess
import logging
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

client_id = "<client-id>"
subscription_id= "<subscription-id>"
credential = DefaultAzureCredential(managed_identity_client_id=client_id)
account_url = "<account-url>"
container_name = "<container-name>"
blob_service_client = BlobServiceClient(account_url, credential)

logging.basicConfig(level=logging.DEBUG)

date_time = datetime.datetime.now()
formated_time = date_time.strftime("%m%d%Y_%H%M%S")

db_config = {
    "db" : "database-name" , 
    "db_host" : "hostname" ,
    "db_user" : "admin" ,
    "db_password" : "password" ,
}

os.environ['PGPASSWORD'] = db_config['db_password']

dbname = db_config["db"]           
backup_file = f"{db_config['db']}_{formated_time}.sql"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=backup_file)

print("starting the process")
cmd = f"pg_dump  -h  {db_config['db_host']} -U {db_config['db_user']} -p 5432 -d {db_config['db']} > {backup_file}"
subprocess.run(cmd, shell=True, check=True)
with open(backup_file, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print(f" Backup of {dbname} uploaded to {container_name}")
