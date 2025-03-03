with open("/Users/arsenijkansin/Documents/labpp2/lab6/dir-and-files/text.txt", "r") as source_file, open("test.txt", "w") as dest_file:

    dest_file.write(source_file.read())

print("File contents copied successfully from text.txt to test.txt.")