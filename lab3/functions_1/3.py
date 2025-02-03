def solve(numheads, numlegs):

    r = (numlegs / 2) - numheads

    c = numheads - r

    return r, c


value_heads = int(input())

value_legs = int(input())

print(solve(value_heads, value_legs))