#This Python code snippet generates a table displaying information about files in a specified directory. It uses the PrettyTable library for creating and formatting the table and the os module to interact with the file system. Here’s a breakdown of what each part does:

#Imports Required Modules:

from prettytable import PrettyTable
import os
# PrettyTable: A library used to create and format tables in a readable way.
# os: A module that provides functions to interact with the operating system, such as file and directory operations.
# Create a tbl object that also defines the headings

tbl = PrettyTable(['FilePath','FileSize'])
# Initializes a PrettyTable object with two column headers: "FilePath" and "FileSize"

DIR = input("Enter Directory Path: ")
#Requests the user to enter the path of the directory they want to scan.

fileList = os.listdir(DIR)
#Retrieves a list of all entries (files and directories) in the specified directory.

for eachFile in fileList:
    filePath = os.path.join(DIR, eachFile)
    absPath  = os.path.abspath(filePath)
    if os.path.isfile(absPath):
        fileSize = os.path.getsize(absPath)
        tbl.add_row( [ absPath, fileSize] )    
#Constructs the full path of each file.
#Converts the path to an absolute path.
#Checks if the path is a file (not a directory).
#Gets the file size in bytes.
#Adds a row to the table with the file’s absolute path and its size.

tbl.align = "l" 
resultString = tbl.get_string(sortby="FileSize", reversesort=True)
print(resultString)
#Sets the alignment of table columns to left ("l").
#Retrieves the table as a string, sorted by "FileSize" in descending order.
#Prints the formatted table.
