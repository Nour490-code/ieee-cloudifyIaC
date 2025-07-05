import boto3
import csv

iam = boto3.client('iam',aws_access_key_id='xxxxxxxx',aws_secret_access_key='xxxx')

with open("Cloudify.csv", newline="") as file:
    reader = csv.reader(file)
    usernames = list(reader)
    usernames = [username[0] for username in usernames][1:]


for username in usernames:
    try:
        print(f"Creating user: {username}")
        iam.create_user(UserName=username)
        iam.create_login_profile(
            UserName=username,
            Password="TemporaryPassword123"        
        )
        iam.add_user_to_group(UserName=username, GroupName="Admin")
        print(f"User {username} created successfully.")
    except Exception as e:
        print(f"Error creating user {username}: {str(e)}")
