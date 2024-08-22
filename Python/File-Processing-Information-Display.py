#This Python script combines several functionalities related to file processing and information display. It demonstrates file reading, directory walking, file hashing, and tabular display using a mix of Python standard libraries and third-party libraries. Here's a detailed breakdown of each section:

#File Reading and Display

import sys

wordList = [] 

print("\nProcessing Book\n")

try:
    with open("test.txt", 'r') as book:
        content = book.read()
        print(content)
except Exception as err:
    print("Exception: ", str(err))
  
#Purpose: Attempts to open and read the contents of a file named test.txt. If an error occurs it prints the error message.


#Directory Walking and File Size Display
import os
import hashlib
from prettytable import PrettyTable

DIR = input("Enter Directory Path: ")

print("Walking: ", DIR, "\n")

tbl = PrettyTable(['FileName', 'FileSize'])

for currentRoot, dirList, fileList in os.walk(DIR):
    for nextFile in fileList:
        fullPath = os.path.join(currentRoot, nextFile)
        absPath = os.path.abspath(fullPath)
        
        print("="*40)
        print("FilePath: ", absPath)
        
        stats = os.stat(absPath)
        fileSize = stats.st_size
        
        tbl.add_row([absPath, fileSize])

tbl.align = "l"
print(tbl.get_string(sortby="FileSize", reversesort=True))
#Walks through a specified directory and its subdirectories, listing all files along with their sizes. It uses the PrettyTable library to display this information in a table sorted by file size in descending order.


#File Hashing
import os
import hashlib
import sys

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
#Prompts the user to enter the path of a file to hash using the SHA-512 algorithm. It reads the file’s contents, computes the hash, and prints the hexadecimal digest. If an error occurs, it exits the script and prints the error message.

#Tabular Display of File Information
from prettytable import PrettyTable

targetFolder = input("Enter Target Folder: ")
print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['FilePath', 'FileSize'])

tbl.add_row(['Testfile.txt', 4096])
tbl.add_row(['junk.bin', 10998])

tbl.align = "l"
print(tbl.get_string(sortby="FileSize", reversesort=True))

for currentRoot, dirList, fileList in os.walk(targetFolder):
    for nextFile in fileList:
        fullPath = os.path.join(currentRoot, nextFile)
        absPath = os.path.abspath(fullPath)
        fileSize = os.path.getsize(absPath)
        
        tbl.add_row([absPath, fileSize])

tbl.align = "l"
print(tbl.get_string(sortby="FileSize", reversesort=True))

print("\nScript-End\n")
#Similar to the previous directory walking section but with some added static data (Testfile.txt and junk.bin) for demonstration purposes. After displaying this static data, it walks through the user-specified target folder, lists all files and their sizes, and displays the information in a sorted table.
#Summary
#Overall, this script performs multiple tasks:

#Reads and displays the contents of a file.
#Walks through a directory to list files and their sizes, displaying them in a formatted table.
#Computes and displays the SHA-512 hash of a user-specified file.
#Demonstrates the ability to combine static and dynamic data in tabular form.
#The script has some issues, such as redundant except blocks and missing sections in the middle, but it showcases basic file and directory operations, error handling, and data presentation using Python libraries.
