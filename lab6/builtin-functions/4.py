import math
import time

num = int(input())
delay = int(input())

time.sleep(delay / 1000)  

print(f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}")
