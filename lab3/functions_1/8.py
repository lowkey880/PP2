def three(lst):

    for i in range(len(lst) - 1):

        if lst[i] == 0 and lst[i + 1] == lst[i] and lst[i + 2] == 7:

            return True

    return False
        
a = int(input("Write a number of elements: "))

list = []

for i in range(a):

    num = int(input("Write an element: "))

    list.append(num)


print(three(list))