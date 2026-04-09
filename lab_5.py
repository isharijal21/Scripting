import os
import subprocess as sp
import shutil
import zipfile as zf
import time
#task 1:backs up files in a directory
def backup_dir(src_dir, dest_dir):
    """Backs up files from source directory to destination directory using rsync."""
    if os.path.exists(src_dir) and os.path.exists(dest_dir):
        print("Backing up files...")
        return_code = sp.call(["rsync", "-av", src_dir, dest_dir])
        if return_code == 0:
            print("Backup completed successfully.")
        else:
            print("Backup failed.")
    else:
        print("Source or destination directory does not exist.")
#Task 2: creates an archive out of the contents of the given directory
def archive_dir(src_dir, arch_type, archive_name):
    """Creates an archive of a directory."""
    acceptable_types = ["zip", "tar", "bztar", "xztar", "gztar"]
    if arch_type in acceptable_types and os.path.exists(src_dir):
        shutil.make_archive(archive_name, arch_type, src_dir)
        print(f"Archive '{archive_name}.{arch_type}' created successfully.")
    else:
        print(f"Invalid archive type '{arch_type}' or source directory doesn't exist.")
"""Task 3:accepts the path to an existing zip file as argument and displays the name
of the operating system from which the file was created and size (in KB) of all files that are greater
than a given threshold (in KB)"""
def read_zip_files(filename, threshold_kb):
    """Displays info about files larger than a threshold from a zip archive."""
    if not os.path.exists(filename):
        print("Zip file does not exist.")
        return

    with zf.ZipFile(filename) as z:
        print(f"Files larger than {threshold_kb} KB:")
        for info in z.infolist():
            file_size_kb = info.file_size / 1024
            if file_size_kb > threshold_kb:
                system_type = "Windows" if info.create_system == 0 else "Unix" if info.create_system == 3 else "Unknown"
                print(f"Name: {info.filename}, Size: {file_size_kb:.2f} KB, Created on: {system_type}")
#Task 4:displays all files in each directory that were modified in the last month
def check_recently_modified_files(directory=None):
    """Displays files modified in the last month in the given directory."""
    if directory is None:
        directory = os.getcwd()
    
    one_month_ago = time.time() - (30 * 24 * 60 * 60)
    
    print(f"Files modified in the last month in '{directory}':")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = os.path.getmtime(file_path)
            if modified_time >= one_month_ago:
                print(file_path)
#menu description
def display_menu():
    """Displays the menu options."""
    print("\nWelcome to the File Tools Menu:")
    print("1. Backup Directory")
    print("2. Create Archive")
    print("3. Read Zip Files")
    print("4. Check Recently Modified Files")
    print("5. Exit")

def main():
    """Main function to run the file tools."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            src_dir = input("Enter source directory path: ")
            dest_dir = input("Enter destination directory path: ")
            backup_dir(src_dir, dest_dir)
        elif choice == "2":
            src_dir = input("Enter source directory path: ")
            arch_type = input("Enter archive type (zip/tar/bztar/xztar/gztar): ")
            archive_name = input("Enter archive name (without extension): ")
            archive_dir(src_dir, arch_type, archive_name)
        elif choice == "3":
            filename = input("Enter zip file path: ")
            threshold_kb = float(input("Enter threshold size in KB: "))
            read_zip_files(filename, threshold_kb)
        elif choice == "4":
            directory = input("Enter directory path (leave blank for current directory): ")
            check_recently_modified_files(directory)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
