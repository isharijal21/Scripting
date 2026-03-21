#!/usr/bash/bin python 
import os

ext_tuple = ('txt', 'png', 'doc', 'dat')
#creates files in the given directory  
def createFiles(fileNamePrefix: str, numOfFiles: int, extension: str) -> None:
    for i in range(1, numOfFiles + 1):
        filename = f"{fileNamePrefix}_{i}.{extension}"
        with open(filename, "w"):
            pass

#gets the type of file 
def getType(fileOrDirectoryPath: str) -> str:
    if os.path.isfile(fileOrDirectoryPath):
        return "File"
    elif os.path.isdir(fileOrDirectoryPath):
        return "Directory"
    else:
        return "Not Found"


#renames the file 
def renameFile(filename: str, newName: str) -> None:
    os.rename(filename, newName)

#creates a new directory in the file 
def createDir(nameOfDirectory: str) -> None:
    os.makedirs(nameOfDirectory, exist_ok=True)
    
    # """For testing only """
    # if os.path.isdir(nameOfDirectory):
    #     os.rmdir(nameOfDirectory)

#creates sub directories 
def createSubDirectories(directoryName: str, numberToCreate: int) -> None:
    if os.path.exists(directoryName):
        subdirectories = [os.path.join(directoryName, f"subdir_{i}") for i in range(1, numberToCreate + 1)]
        for subdir in subdirectories:
            os.makedirs(subdir, exist_ok=True)
        
        # # For testing only
        # for subdir in subdirectories:
        #     if os.path.isdir(subdir):
        #         os.rmdir(subdir)


#renames the file with the new extension 
def renameFiles(targetDirectory: str, currentExt: str, newExt: str) -> None:
    for file_name in os.listdir(targetDirectory):
        # Split the filename into name and extension
        name, ext = os.path.splitext(file_name)
        new_file_name = f"{name}.{newExt}"
        
        # Rename the file
        os.rename(os.path.join(targetDirectory, file_name),
                    os.path.join(targetDirectory, new_file_name))


#prints the content 
def displayContents(directoryName: str) -> None:
    print(f"Name\tType")
    print("-------\t------")
    for entry in os.listdir(directoryName):
        entry_path = os.path.join(directoryName, entry)
        entry_type = getType(entry_path)
        print(f"{entry}\t{entry_type}")

def main():
    # Part a
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}")

    # Part b
    username = os.getlogin()
    cit_directory = f"CITSpring2024_{username}"
    createDir(cit_directory)
    print(f"New Directory made: {cit_directory}")

    # Part d
    num_of_files = int(input("Enter the number of files: "))
    if num_of_files <= 0:
        print("Error: Number of files cannot be negative or zero.")
    else:
        user_extension = input("Enter the extension (txt/png/doc/dat): ")
        if user_extension not in ext_tuple:
            print("Error: Wrong file extension.")
        else:
            createFiles(cit_directory, num_of_files, user_extension)
            print(f"{num_of_files} files created.")

    # Part e
    num_of_subdirectories = int(input("Enter the number of subdirectories: "))
    if num_of_subdirectories <= 0:
        print("Error: Number of subdirectories cannot be negative or zero.")
    else:
        createSubDirectories(cit_directory, num_of_subdirectories)
        print(f"{num_of_subdirectories} subdirectories created.")

    # Part f
    displayContents(current_directory)
    print ("\n \n")
    
    # Part g
    new_ext = input("Enter the new extension (txt/png/doc/dat): ")
    if new_ext not in ext_tuple:
        print("Error: Wrong file extension.")
    else:
        renameFiles(cit_directory, user_extension, new_ext)
        print("Files renamed.")

    # Part h
    displayContents(cit_directory)

if __name__ == "__main__":
    main()
