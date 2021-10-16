import sys
import math

states = []
states.append(False)# [0] is for circuit inverters state
states.append(False)# [1] is for the beer state


l, c = [int(i) for i in input().split()]
mapa = []
tele = []
prints = []
for i in range(l):
    mapa.append(input())
    if mapa[i].find("@") != -1:
        bender_pos = [int(mapa[i].find("@")), i]
    if mapa[i].find("T") != -1:
        tele.append([int( mapa[i].find("T")), i])

next_move = []
next_move.append(1)# 1 is South; 2 is E; 3 is N; 4 is W

count = []
count.append(0)

def f_next_move(move):
    if move == 1:
        return "SOUTH", 0, 1
    elif move == 2:
        return "EAST", 1, 0
    elif move == 3:
        return "NORTH", 0, -1
    elif move == 4:
        return "WEST", -1, 0

def find_path(start):
    x = bender_pos[0]
    y = bender_pos[1]
    if start == 5: start = 1
    if start == 0: start = 4
    direction, x1, y1 = f_next_move(start)
    if states[0] == False:
        if mapa[y+y1][x+x1] == "#" or mapa[y+y1][x+x1] == "X":
            return find_path((start+1))
        elif mapa[y+y1][x+x1] == " ":
            next_move[0] = start
            return direction, x1, y1, False
        else:
            next_move[0] = start
            look_for_directions(mapa[y+y1][x+x1])
            return direction, x1, y1, True
    else:
        if mapa[y+y1][x+x1] == "#" or mapa[y+y1][x+x1] == "X":
            return find_path((start-1))
        elif mapa[y+y1][x+x1] == " ":
            next_move[0] = start
            return direction, x1, y1, False
        else:
            next_move[0] = start
            look_for_directions(mapa[y+y1][x+x1])
            return direction, x1, y1, True

def f_path_modifiers(where):
    if where == "S":
        dire = 1
    elif where == "E":
        dire = 2
    elif where == "N":
        dire = 3
    elif where == "W":
        dire = 4
    next_move[0] = dire
    return f_next_move(dire)

def f_prints(di):
    prints.append(di)
    in_loop = False
    if len(prints) > 50:
        in_loop = True
        string1 = di
        string2 = ""
        for k in range(40):
            if string1 != prints[len(prints) - 1 - k] and string2 == "":
                string2 = prints[len(prints) - 1 - k]
            elif string1 != prints[len(prints) - 1 - k] and string2 != prints[len(prints) - 1 - k]:
                in_loop = False
    if in_loop:
        count[0] += 1
        print("LOOP")
    return in_loop


def look_for_directions(letra = ""):
    x = bender_pos[0]
    y = bender_pos[1]
    flag2 = False
    print(f"{x=}" + f"; {y=}", file=sys.stderr, flush=True)
    direction, x1, y1 = f_next_move(next_move[0])
    if mapa[y+y1][x+x1] == "$" or letra == "$":
        f_prints(direction)
        flag2 = True
    elif mapa[y+y1][x+x1] == " ":
        flag2 = f_prints(direction)
    elif mapa[y+y1][x+x1] == "E" or mapa[y+y1][x+x1] == "N" or mapa[y+y1][x+x1] == "W" or mapa[y+y1][x+x1] == "S" or letra == "E" or letra == "N" or letra == "W" or letra == "S":
        flag2 = f_prints(direction)
        bender_pos[0] += x1
        bender_pos[1] += y1
        direction2, x1, y1 = f_path_modifiers(mapa[y+y1][x+x1])
        x1 = y1 = 0
    elif mapa[y+y1][x+x1] == "#" or mapa[y+y1][x+x1] == "X":
        if mapa[y+y1][x+x1] == "X" and states[1] == True:
            mapa[y+y1] = mapa[y+y1][:x+x1] + " " + mapa[y+y1][x+x1+1:]# Breaks the block
            f_prints(direction)
        elif states[0] == False:
            direction2, x1, y1, flag2 = find_path(1)
            if flag2 == False: f_prints(direction2)
        elif states[0] == True:
            direction2, x1, y1, flag2 = find_path(4)
            if flag2 == False: f_prints(direction2)
    elif mapa[y+y1][x+x1] == "I" or letra == "I":
        flag2 = f_prints(direction)
        states[0] = True if states[0] == False else False
    elif mapa[y+y1][x+x1] == "B" or letra == "B":
        flag2 = f_prints(direction)
        states[1] = True if states[1] == False else False
    elif mapa[y+y1][x+x1] == "T" or letra == "T":
        flag2 = f_prints(direction)
        print("Tele", file=sys.stderr, flush=True)
        if tele[0][0] == x+x1 and tele[0][1] == y+y1:
            bender_pos[0] = tele[1][0]
            bender_pos[1] = tele[1][1]
        elif tele[1][0] == x+x1 and tele[1][1] == y+y1:
            bender_pos[0] = tele[0][0]
            bender_pos[1] = tele[0][1]
        x1 = y1 = 0

    bender_pos[0] += x1
    bender_pos[1] += y1
    if flag2 == False: look_for_directions()

look_for_directions()

if count[0] == 0:
    for pr in prints:
        print(pr)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
