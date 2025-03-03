text = input()

sum_upper = sum(map(str.isupper, text))

sum_lower = sum(map(str.islower, text))

print("Upper case letters: ", sum_upper)

print("Lower case letters: ", sum_lower)