my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

with open("/Users/arsenijkansin/Documents/labpp2/lab6/dir-and-files/text.txt", "w") as file:

    for item in my_list:

        file.write(item + "\n")

print("List has been written to text.txt")