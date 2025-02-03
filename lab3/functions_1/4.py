def prime(num):

    if num <= 1:

        return False
    
    for i in range(2, num - 1):

        if num % i == 0:

            return False
        
    return True

def filter(list):

    return [num for num in list if prime(num)]



value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(filter(value_list))