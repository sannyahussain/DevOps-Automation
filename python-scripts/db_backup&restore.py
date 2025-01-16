#import the libraries
import yaml
import psycopg2
import subprocess
import sys

#will read the configurations from the config.yaml file, upon user input

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

input_var = input("Enter the Hostname (local, dev, stage) : ")
database = input("Enter DB Name for Dump : ")
dump_file_name = input("Enter the Dump Filename : ")

server_config = config.get(input_var)
if server_config :
    print("Backup Started")
    cmd = f"pg_dump -h {server_config['host']} -U {server_config['user']} -p 5432 -d {database} -Fc -f {dump_file_name} "
    subprocess.run(cmd, shell=True, check=True, env={"PGPASSWORD" : server_config["password"]})
    print("backup has been completed")

else:
    print("Invalid Server Name")
    sys.exit()

target_host = input("Enter the Hostname to create database (local, dev, stage) : ")
target_database = input("Enter the Name to create empty Database : ")

target_server_config = config.get(target_host)
if target_server_config:

    target_db_conn = psycopg2.connect(

    host = target_server_config['host'],
    user = target_server_config['user'],
    password = target_server_config['password'],
    database = "postgres"
)


    target_db_conn.autocommit = True

    db = target_db_conn.cursor()
    db.execute(f"CREATE DATABASE {target_database}")
    print("database has been created")
    target_db_conn.close()

    print("Database Restore Started")
    cmd_restore = f"pg_restore -h  {target_server_config['host']} -U {target_server_config['user']} -p 5432 -d {target_database} {dump_file_name}"
    subprocess.run(cmd_restore, shell=True, check=True, env = {'PGPASSWORD' : target_server_config['password']})
    print("Restore has been completed")
else:
    print("Invalid Server Name")
    sys.exit()
