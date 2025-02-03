def three(lst):

    for i in range(len(lst) - 1):

        if lst[i] == 3 and lst[i + 1] == 3:

            return True

    return False
        
a = int(input("Write a number of elements: "))

list = []

for i in range(a):

    num = int(input("Write an element: "))

    list.append(num)


print(three(list))