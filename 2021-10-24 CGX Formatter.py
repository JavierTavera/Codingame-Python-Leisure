import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
strings = ""
for i in range(n):
    cgxline = input().strip()
    strings += cgxline
    #strings.append(input())

new_string = ""
nr_of_jumps = 0
#fisrt_st = False
for st in strings:
    len_st = len(new_string)
    if st == " ":
        pass
    elif st == "(":
        #nr_of_jumps += 1
        if len_st > 0 and new_string[len_st-1] == "=":
            new_string += "\n" + "    "*nr_of_jumps + st+ "\n" + "    "*(nr_of_jumps + 1)
            nr_of_jumps += 1
        else:
            nr_of_jumps += 1
            new_string += st + "\n" + "    "*nr_of_jumps
    elif st == ")" and new_string[-6:] == "(\n    ":
        nr_of_jumps -= 1
        len_st -= 5
        new_string = new_string[:len_st] + "\n)"
    elif st == ")":
        nr_of_jumps -= 1
        new_string += "\n" + "    "*nr_of_jumps + st
    elif st == ";":
        new_string += st + "\n" + "    "*nr_of_jumps
    else:
        new_string +=  st
print(new_string, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(new_string)
