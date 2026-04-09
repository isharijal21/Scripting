#!usr/bin/python

import argparse as arg
import os

def list_directory_contents(directory_path, log_file=None, list_only_directories=False):
    try:
        # Check if directory exists
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")
        
        # Open log file if specified
        if log_file:
            with open(log_file, 'w') as f:
                print(f"Listing contents of directory '{directory_path}':", file=f)
                print("************************************************************", file=f)
                print()

                # List directory contents
                count = 0
                for entry in os.listdir(directory_path):
                    if entry not in ['.', '..']:
                        if os.path.isdir(os.path.join(directory_path, entry)):
                            if not list_only_directories:
                                count += 1
                                print(f"{count}. {entry}", file=f)
                        elif not list_only_directories:
                            count += 1
                            print(f"{count}. {entry}", file=f)

                print("************************************************************", file=f)
                print(f"Total: {count} entries", file=f)
                print("************************************************************", file=f)
                print("Listing completed successfully.", file=f)

        else:
            # Output to console
            print(f"Listing contents of directory '{directory_path}':")
            print("************************************************************")
            print()

            # List directory contents
            count = 0
            for entry in os.listdir(directory_path):
                if entry not in ['.', '..']:
                    if os.path.isdir(os.path.join(directory_path, entry)):
                        if not list_only_directories:
                            count += 1
                            print(f"{count}. {entry}")
                    elif not list_only_directories:
                        count += 1
                        print(f"{count}. {entry}")

            print("************************************************************")
            print(f"Total: {count} entries")
            print("************************************************************")
            print("Listing completed successfully.")
    
    except Exception as e:
        if log_file:
            with open(log_file, 'a') as f:
                print(f"Error: {str(e)}", file=f)
        else:
            print(f"Error: {str(e)}")

def main():
    # Setup option parser
    parser = arg.ArgumentParser(description="List contents of a directory.")
    parser.add_argument("-i", "--logfile", help="Specify the log file name.")
    parser.add_argument("-d", "--dir", required=True, help="Specify the directory path.")
    args = parser.parse_args()

    # Check for directory existence
    directory_path = args.dir
    log_file = args.logfile

    # List only directories if specified
    list_only_directories = False
    if directory_path:
        if os.path.isdir(directory_path):
            list_directory_contents(directory_path, log_file=log_file, list_only_directories=list_only_directories)
        else:
            print(f"Error: Directory '{directory_path}' not found.")
    else:
        print("Error: Directory path not provided.")

if __name__ == "__main__":
    main()
