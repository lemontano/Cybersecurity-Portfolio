import sys
import os
import hashlib
from prettytable import PrettyTable

# 1. File Reading and Display
wordList = [] 

print("\nProcessing Book\n")

try:
    with open("test.txt", 'r') as book:  # Ensure test.txt is in the same directory or provide an absolute path.
        content = book.read()
        print(content)
except Exception as err:
    print("Exception: ", str(err))

# 2. Directory Walking and File Size Display (Consolidated)
def walk_directory_and_display_files(directory):
    try:
        print("Walking: ", directory, "\n")

        tbl = PrettyTable(['FileName', 'FileSize'])

        for currentRoot, dirList, fileList in os.walk(directory):
            for nextFile in fileList:
                fullPath = os.path.join(currentRoot, nextFile)
                absPath = os.path.abspath(fullPath)
                
                stats = os.stat(absPath)
                fileSize = stats.st_size

                # Add file information to the table
                tbl.add_row([absPath, fileSize])

        tbl.align = "l"
        print(tbl.get_string(sortby="FileSize", reversesort=True))
    
    except Exception as err:
        print("Error processing directory:", str(err))

# 3. File Hashing using SHA-512
def hash_file():
    while True:
        fileToHash = input("\nFile to Hash >>> ")
        if os.path.isfile(fileToHash):
            break
        else:
            print("\nInvalid File ... Please Try Again")

    try:
        print("\nAttempting to hash file: ", fileToHash)
        
        with open(fileToHash, 'rb') as target:
            fileContents = target.read()
            sha512Obj = hashlib.sha512()
            sha512Obj.update(fileContents)
            hexDigest = sha512Obj.hexdigest()

            print("\n\n", fileToHash, " SHA-512 Hex Digest = ", hexDigest, "\n\n")
    except Exception as err:
        sys.exit("\nException: " + str(err))

# 4. Main Flow
def main():
    # 1. Read and display contents of a file (test.txt)
    print("Reading and displaying contents of test.txt...")
    
    # 2. Walking a directory to display file sizes
    dir_path = input("Enter Directory Path: ")
    walk_directory_and_display_files(dir_path)

    # 3. File Hashing
    hash_file()

    # 4. Second directory walk (optional, based on your requirements)
    target_folder = input("Enter Target Folder: ")
    walk_directory_and_display_files(target_folder)

    print("\nScript-End\n")

# Run the script
if __name__ == "__main__":
    main()

print("\nScript-End\n")
#Similar to the previous directory walking section but with some added static data (Testfile.txt and junk.bin) for demonstration purposes. After displaying this static data, it walks through the user-specified target folder, lists all files and their sizes, and displays the information in a sorted table.
#Summary
#Overall, this script performs multiple tasks:

#Reads and displays the contents of a file.
#Walks through a directory to list files and their sizes, displaying them in a formatted table.
#Computes and displays the SHA-512 hash of a user-specified file.
#Demonstrates the ability to combine static and dynamic data in tabular form.
#The script has some issues, such as redundant except blocks and missing sections in the middle, but it showcases basic file and directory operations, error handling, and data presentation using Python libraries.
