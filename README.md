# DevOps Automation Scripts

This repository contains a collection of DevOps automation scripts and configurations to streamline daily tasks and some server configuration including:

- **Database Backup & Restoration**: Scripts for automating database backups and restores.
- **CI/CD Pipelines**: Configuration for continuous integration and deployment,using GitHub Actions.
- **SonarQube Integration**: Setup files for integrating SonarQube with CI/CD pipelines for code quality analysis.
- **Server Automation**: Scripts for managing cloud-based infrastructure and servers, including starting, stopping, and managing Azure resources.

# Database Backups:
- Go to the folder python-scripts and edit the file db_backups.py save and run where you want to keep the backups.

# Usage:
This script automates the process of backing up two PostgreSQL databases. It uses pg_dump to create backups and saves them as .sql files with a timestamp in a specified directory. The script uses environment variables to securely handle the database password. 

# Database Dump and Restore Script:
- Nevigate to the python-scripts folder and edit the db_backup&restore.py file , change the variable names before runing the script.

# Usage:

This script performs both database dumping and restoration. It first takes a backup of a specified PostgreSQL database by connecting to a given server, then stores the dump in a specified file. The script also allows the creation of a new empty database on a target server and restores the dumped data into it. Configuration details are read from a YAML file for flexible server management.


# Database Backup and Upload to Azure Blob Storage

# Overview

This script automates the backup of a PostgreSQL database and uploads the backup file to an Azure Blob Storage container using Azure Managed Identity for authentication.

Prerequisites

- Python 3.x installed

- PostgreSQL installed with pg_dump available

- Azure Storage Blob Python SDK (azure-identity, azure-storage-blob)

- Azure Managed Identity with appropriate permissions to access Blob Storage

# Installation

- pip install azure-identity azure-storage-blob

Ensure your environment is configured for Azure authentication using Managed Identity.

# Configuration

Update the following placeholders in the script:

client_id = "<client-id>"
subscription_id= "<subscription-id>"
account_url = "<account-url>"
container_name = "<container-name>"

# Database Configuration
db_config = {
    "db" : "database-name", 
    "db_host" : "hostname",
    "db_user" : "admin",
    "db_password" : "password",
}

# Usage

Run the script:

python db_storageaccount.py

# Script Workflow

- Generates a timestamped backup filename.

- Sets up authentication using Azure Managed Identity.

- Exports the PostgreSQL database using pg_dump.

- Uploads the backup file to Azure Blob Storage.

- Logs the backup process.

# Logging

Logging is enabled at DEBUG level for tracking the process. Modify logging.basicConfig(level=logging.DEBUG) to adjust verbosity.
