import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
inUnary = ""
count01 = 0

completeBinary = ""
for i in message:
    toASCII = ord(i)
    toBinary = bin(toASCII)[2:]
    if len(toBinary) < 7:
        toBinary = "0" + toBinary
    completeBinary += toBinary

is0or1 = 2

for j in completeBinary:
    if int(j) == 0:
        if is0or1 != 2 and is0or1 != 0:
            inUnary += "0 "
            for k in range(count01):
                inUnary += "0"
            inUnary += " "
            count01 = 0
        
        is0or1 = 0
        count01 += 1

    else:
        if is0or1 != 2 and is0or1 != 1:
            inUnary += "00 "
            for k in range(count01):
                inUnary += "0"
            inUnary += " "
            count01 = 0
        
        is0or1 = 1
        count01 += 1
        
if is0or1 == 1:
    inUnary += "0 "
else:
    inUnary += "00 "

for l in range(count01):
    inUnary += "0"


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(inUnary)
