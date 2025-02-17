def generate_num(N):

    for i in range(N, 0, -1):

        yield i  

N = int(input())

for num in generate_num(N):
    
    print(num)