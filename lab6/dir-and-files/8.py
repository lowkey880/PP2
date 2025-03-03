import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):

    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):

        os.remove(file_path)

        print(f"File '{file_path}' has been deleted successfully.")
    else:

        print("Error: You don't have permission to delete this file.")
else:

    print("Error: The specified file does not exist.")

#/Users/arsenijkansin/Documents/labpp2/lab6/dir-and-files/text.txt