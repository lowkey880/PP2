def pol(example):

    rev = example[::-1]

    return rev == example

word = str(input("Write a word: "))

print(pol(word))