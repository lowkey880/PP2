a = int(input("Write a number of elements: "))

lst = []

for i in range(a):

    num = int(input("Write an element of list: "))

    lst.append(num)

prime_numbers = list(filter(lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1, lst))

print("Prime numbers:", prime_numbers)