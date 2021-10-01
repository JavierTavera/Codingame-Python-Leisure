import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

while(r_1 != r_2):
    num = 0
    if r_1 < r_2:
        for i in str(r_1): num += int(i)
        r_1 += num
    else:
        for i in str(r_2): num += int(i)
        r_2 += num

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(r_1)
