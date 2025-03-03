def all_elements_true(t):
    return all(t)

n = int(input())
tuple_values = tuple(int(input()) for i in range(n))

print(all_elements_true(tuple_values))
