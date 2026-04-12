#!/usr/bin/env python3

import argparse
from ftplib import FTP
import os

# Function to upload a file to VM2
def upload_file(server_ip, filename):
    try:
        # Connect to the FTP server
        ftp = FTP(server_ip)
        ftp.login(user='student', passwd='password')  # You'd use your own credentials here

        # Check if the file exists locally
        if os.path.exists(filename):
            remote_path = 'cit383F2023/' + os.path.basename(filename)
            with open(filename, 'rb') as local_file:
                ftp.storbinary('STOR ' + remote_path, local_file)
            print(f"File '{filename}' uploaded successfully to VM2.")
        else:
            print(f"Error: File '{filename}' does not exist locally.")

        ftp.quit()  # Close the FTP connection
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to download files from VM2 based on file extension
def download_files(server_ip, file_extension):
    try:
        # Connect to the FTP server
        ftp = FTP(server_ip)
        ftp.login(user='student', passwd='password')  # Your own login credentials would go here

        # Change to the appropriate directory and get the file list
        ftp.cwd('cit383F2023')
        files = ftp.nlst()

        # Filter files based on the given extension and download them
        matching_files = [file for file in files if file.endswith(file_extension)]
        if matching_files:
            for file in matching_files:
                local_path = os.path.join(os.getcwd(), file)
                with open(local_path, 'wb') as local_file:
                    ftp.retrbinary('RETR ' + file, local_file.write)
            print(f"Files with extension '{file_extension}' downloaded successfully from VM2.")
        else:
            print(f"No files found with extension '{file_extension}' on VM2.")

        ftp.quit()  # Close the FTP connection
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to execute 'ls' command on VM2 and list files of a certain type
def exec_command(server_ip, file_type):
    try:
        # Connect to the FTP server
        ftp = FTP(server_ip)
        ftp.login(user='student', passwd='password')  # Your login credentials would be inserted here

        # Change directory and list files based on file type
        ftp.cwd('cit383F2023')
        files = ftp.nlst()
        matching_files = [file for file in files if file.endswith(file_type)]

        # Display matching files or indicate if none are found
        if matching_files:
            print(f"Files with extension '{file_type}':")
            print("-----------------------------")
            for file in matching_files:
                print(file)
        else:
            print(f"No files found with extension '{file_type}' on VM2.")

        ftp.quit()  # Close the FTP connection
    except Exception as e:
        print(f"Error: {str(e)}")

# Parsing command-line arguments
parser = argparse.ArgumentParser(description='FTP Operations Script')
parser.add_argument('FTP_SERVER_IP', help='IP address of the FTP server')
parser.add_argument('-u', '--upload', metavar='filename', help='Upload the specified file to VM2')
parser.add_argument('-d', '--download', metavar='fileExtension', help='Download files with specified extension')

args = parser.parse_args()

if args.upload:
    upload_file(args.FTP_SERVER_IP, args.upload)
elif args.download:
    download_files(args.FTP_SERVER_IP, args.download)
else:
    parser.print_help()
