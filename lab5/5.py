import re

with open("/Users/arsenijkansin/Documents/labpp2/lab5/row.txt", "r") as file:
    text = file.read()
x = re.findall(r"a.+b", text)

print(x)