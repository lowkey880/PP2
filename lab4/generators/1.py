def generate_sq(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input())

for i in generate_sq(n):
    print(i, end = " ")