from flask import Flask, request, jsonify
import pymysql
import boto3
import os

app = Flask(__name__)

# AWS RDS Database configuration
DB_HOST = "xxxxx.us-east-1.rds.amazonaws.com"
DB_USER = "xxx"
DB_PASSWORD = "xxx"
DB_NAME = "myapp_db"

# AWS S3 Configuration
S3_BUCKET = "cloudify-tesht"
AWS_ACCESS_KEY = "xxxxx"
AWS_SECRET_KEY = "xxxxx"

# Initialize S3 client
s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Upload file to S3 and save metadata to RDS
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    # Upload file to S3
    s3.upload_fileobj(file, S3_BUCKET, file.filename)
    
    # Save file metadata to RDS
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO files (filename) VALUES (%s)", (file.filename,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200

# Get list of uploaded files
@app.route("/files", methods=["GET"])
def list_files():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM files")
    files = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    return jsonify({"files": files}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
