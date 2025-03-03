import os

def check_path_access(path):

    if os.path.exists(path):

        print(f"\nPath: {path}")

        print("Exists: Yes")

        print("Readable:", "Yes" if os.access(path, os.R_OK) else "No")

        print("Writable:", "Yes" if os.access(path, os.W_OK) else "No")

        print("Executable:", "Yes" if os.access(path, os.X_OK) else "No")

    else:

        print("Error: The specified path does not exist.")

specified_path = input("Enter the directory or file path: ")

check_path_access(specified_path)