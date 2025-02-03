def set(lst):

    set_list = []

    for i in range(len(lst)):

        if lst[i] not in set_list:

            set_list.append(lst[i])

    return set_list 

a = int(input("Write a number of elements in list: "))

list_num = []

for i in range(a):

        num = int(input("write an element of list: "))

        list_num.append(num)

print(set(list_num))