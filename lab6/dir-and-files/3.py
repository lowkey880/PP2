import os

def check_path(path):

    if os.path.exists(path):

        print(f"Path: {path}")

        print("Path exists!")

        print("Directory:", os.path.dirname(path))

        print("Filename:", os.path.basename(path))

    else:

        print("Error: The specified path does not exist.")

specified_path = input("Enter the file or directory path: ")

check_path(specified_path)
#/Users/arsenijkansin/Documents/labpp2/lab6/dir-and-files