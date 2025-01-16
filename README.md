# DevOps Automation Scripts

This repository contains a collection of DevOps automation scripts and configurations to streamline daily tasks and some server configuration including:

- **Database Backup & Restoration**: Scripts for automating database backups and restores.
- **CI/CD Pipelines**: Configuration for continuous integration and deployment,using GitHub Actions.
- **SonarQube Integration**: Setup files for integrating SonarQube with CI/CD pipelines for code quality analysis.
- **Server Automation**: Scripts for managing cloud-based infrastructure and servers, including starting, stopping, and managing Azure resources.

Database Backups:
- Go to the folder python-scripts and edit the file db_backups.py save and run where you want to keep the backups.

Usage:
This script automates the process of backing up two PostgreSQL databases. It uses pg_dump to create backups and saves them as .sql files with a timestamp in a specified directory. The script uses environment variables to securely handle the database password. 

Database Dump and Restore Script:
- Nevigate to the python-scripts folder and edit the db_backup&restore.py file , change the variable names before runing the script.

Usage:

This script performs both database dumping and restoration. It first takes a backup of a specified PostgreSQL database by connecting to a given server, then stores the dump in a specified file. The script also allows the creation of a new empty database on a target server and restores the dumped data into it. Configuration details are read from a YAML file for flexible server management.


