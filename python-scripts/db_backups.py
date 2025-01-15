import datetime
import os
import subprocess
import logging

date_time = datetime.datetime.now()
formated_time = date_time.strftime("%m%d%Y_%H%M%S")

db_config = {
        "db1" : "your-db-name" , 
        "db2" : "your-db-name" , 
        "db_host" : "your-hostname" ,
        "db_user" : "your-username" ,
        "db_password" : "password" ,
        "file_path" : "your-file-path"
        }
os.chdir(db_config['file_path'])
os.environ['PGPASSWORD'] = db_config['db_password']

for x in ['db1', 'db2']:
     dbname = db_config[x]           
     backup_file = f"{dbname}_{formated_time}.sql"
     print("starting the process")
     cmd = f"pg_dump  -h  {db_config['db_host']} -U {db_config['db_user']} -p 5432 -d {dbname} > {backup_file}"
     subprocess.run(cmd, shell=True, check=True)
     print(f" Backup of {dbname} saved to {db_config['file_path']}")