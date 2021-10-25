
n = int(input())
strings = ""
for i in range(n):
    strings += input().strip()

new_string = ""
nr_of_jumps = 0
last_is_open_apostrophe = False
last_is_parenthesis = False
#before_parenthesis = 0

for st in strings:
    len_st = len(new_string)
    if last_is_open_apostrophe and st != "'":
        new_string +=  st
    elif st == "(":
        last_is_parenthesis = True
        if len_st > 0 and new_string[len_st-1] == "=":
            new_string += "\n" + "    "*nr_of_jumps + st+ "\n" + "    "*(nr_of_jumps + 1)
            nr_of_jumps += 1
        elif len_st > 0 and new_string[len_st-1].isalpha():
            new_string += st
        else:
            nr_of_jumps += 1
            new_string += st + "\n" + "    "*nr_of_jumps

    elif st == ")":
        if last_is_parenthesis and not new_string[len_st-2].isalpha():
            len_st = len_st -1 - 4*nr_of_jumps
            nr_of_jumps -= 1
            new_string = new_string[:len_st] + "\n" + "    "*nr_of_jumps + ")"
        elif  len_st > 1 and new_string[len_st-2].isalpha() and new_string[len_st-1] == "(":
            new_string += st
        else:
            nr_of_jumps -= 1
            new_string += "\n" + "    "*nr_of_jumps + st
        last_is_parenthesis = False

    elif st == ";":
        last_is_parenthesis = False
        new_string += st + "\n" + "    "*nr_of_jumps
    elif st == " " or st == "	" or st == "\n":
        #last_is_parenthesis = False
        if last_is_open_apostrophe:
            new_string +=  st

    else:
        last_is_parenthesis = False
        if st == "'":
            #before_parenthesis += 1
            last_is_open_apostrophe = not last_is_open_apostrophe
        new_string +=  st

print(new_string)
