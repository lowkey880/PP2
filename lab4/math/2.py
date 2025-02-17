import math
def areaT(h, b1, b2):
    return 0.5 * (b1 + b2) * h

height = float(input())
base1 = float(input())
base2 = float(input())

print(areaT(height, base1, base2))