import math

def multiply_list(numbers):
    return math.prod(numbers)  

a = int(input())
lst = []
for i in range(a):
    l = int(input())
    lst.append(l)

result = multiply_list(lst)
print("Product of all numbers in the list:", result)