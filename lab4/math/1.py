import math
def convert(n):
    radian = n * math.pi / 180
    return radian

l = int(input())
print(round(convert(l), 6))
