# DevOps Automation Scripts

This repository contains a collection of DevOps automation scripts and configurations to streamline daily tasks and some server configuration including:

- **Database Backup & Restoration**: Scripts for automating database backups and restores.
- **CI/CD Pipelines**: Configuration for continuous integration and deployment,using GitHub Actions.
- **SonarQube Integration**: Setup files for integrating SonarQube with CI/CD pipelines for code quality analysis.
- **Server Automation**: Scripts for managing cloud-based infrastructure and servers, including starting, stopping, and managing Azure resources.

The goal of this repo is to provide reusable automation templates for efficient DevOps operations.

**Database Backups: **
This script automates the process of backing up two PostgreSQL databases. It uses pg_dump to create backups and saves them as .sql files with a timestamp in a specified directory. The script uses environment variables to securely handle the database password. 

Go to the folder python-scripts and edit the file db_backups.py save and run where you want to keep the backups.

## Usage

Clone the repository and navigate to the respective folders for individual setups. Each section contains detailed instructions on configuration and usage.

