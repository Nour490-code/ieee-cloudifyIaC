# Cloudify IEEE Event Project

## Overview

This repository contains two main components for the IEEE Cloudify event:

1. **IAM User Creation Script** (`iam-users-script/`):  
   Automates the creation of AWS IAM users for each student attendee, based on a provided CSV list.

2. **Cloudify Project Example** (`project/`):  
   A sample cloud application for students to implement during the session, demonstrating file upload to AWS S3 and metadata storage in AWS RDS, with a simple client GUI.

---

## 1. IAM User Creation Script

- **Location:** `iam-users-script/`
- **Files:**
  - `iam.py`: Python script that reads student registration numbers from `Cloudify.csv` and creates an AWS IAM user for each, assigns a temporary password, and adds them to the "Admin" group.
  - `Cloudify.csv`: CSV file with a list of registration numbers (one per line, header: "Registration Number").

- **How it works:**
  - Uses `boto3` to interact with AWS IAM.
  - For each student in the CSV, creates a user, sets a login profile with a default password, and adds the user to the "Admin" group.
  - Errors are printed if user creation fails.

---

## 2. Cloudify Project Example

- **Location:** `project/`
- **Files:**
  - `app.py`: Flask web server with two endpoints:
    - `/upload` (POST): Uploads a file to AWS S3 and saves the filename in an AWS RDS MySQL database.
    - `/files` (GET): Lists all uploaded filenames from the database.
  - `client.py`: Simple Tkinter GUI client for uploading files and listing uploaded files via the Flask API.
  - `requirements.txt`: Lists Python dependencies (`Flask`, `pymysql`, `boto3`).
  - `Dockerfile`: Containerizes the Flask app for easy deployment.

- **Technologies Used:**
  - **Flask:** For the web API.
  - **boto3:** For AWS S3 integration.
  - **pymysql:** For MySQL (RDS) database access.
  - **Tkinter:** For the desktop client GUI.
  - **Docker:** For containerization.

- **How it works:**
  - **Backend (`app.py`):**
    - Receives file uploads, stores them in S3, and records metadata in RDS.
    - Provides an endpoint to list all uploaded files.
  - **Client (`client.py`):**
    - GUI for selecting and uploading files.
    - Button to list all uploaded files.
    - Communicates with the Flask API.

---

## Folder Structure

```
Cloudify/
│
├── iam-users-script/
│   ├── iam.py
│   └── Cloudify.csv
│
└── project/
    ├── app.py
    ├── client.py
    ├── requirements.txt
    └── Dockerfile
```

--- 