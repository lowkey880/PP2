import os

def list_items(path):
    
    all_items = os.listdir(path)

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]

    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", directories)

    print("Files:", files)

    print("All Items:", all_items)

specified_path = input("Enter the directory path: ")

if os.path.exists(specified_path):

    list_items(specified_path)

else:
    
    print("Error: The specified path does not exist.")

# /Users/arsenijkansin/Documents/labpp2/lab6
# /Users/arsenijkansin/Documents/labpp2/lab6/dir-and-files


