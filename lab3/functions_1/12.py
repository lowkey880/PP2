def histogram(lst):

    for i in lst:
            
        print("*" * i)

        
    
a = int(input("Write a number of list elements: "))

list = []

for i in range(a):

    num = int(input("Write an elemnt of list: "))

    list.append(num)
    
histogram(list)