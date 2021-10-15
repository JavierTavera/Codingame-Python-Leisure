# Este es sólo el inicio
import sys
import math

start_state = 1# starts in @ and heads south
suicide_booth = 2# dies when reaching $
obstacles_state = 3# represented by # or X
encounters_obstacle = 4# he changes direction. Priorities: SOUTH, EAST, NORTH and WEST
path_modifiers= 5# The S modifier will make him turn SOUTH from then on, E, to the EAST, N to the NORTH and W to the WEST.
circuit_inverters = 6# Priorities will become WEST, NORTH, EAST, SOUTH
beer_state = 7# B. Can destroy and pass through X
teleport_state = 8# T
space_state = 9# blank areas

currentState = []
currentState.append(start_state)

states = []
states.append(False)# [0] is for circuit inverters state
states.append(False)# [1] is for the beer state


l, c = [int(i) for i in input().split()]
mapa = []
for i in range(l):
    mapa.append(input())
    if mapa[i].find("@") != -1:
        bender_pos = [int(mapa[i].find("@")), i]

next_move = []
next_move.append(1)# 1 is South; 2 is E; 3 is N; 4 is W

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
        else:
            next_move[0] = start
            return f_next_move(start)
    else:
        if mapa[y+y1][x+x1] == "#" or mapa[y+y1][x+x1] == "X":
            return find_path((start-1))
        else:
            next_move[0] = start
            return f_next_move(start)

def f_path_modifiers(where):
    print(f"{where=}", file=sys.stderr, flush=True)
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


def look_for_directions(cState = currentState[0]):
    x = bender_pos[0]
    y = bender_pos[1]
    print(f"{x=}" + f" {y=}", file=sys.stderr, flush=True)
    direction, x1, y1 = f_next_move(next_move[0])
    #print(f"{cState=}", file=sys.stderr, flush=True)
    print(f"{mapa[y+y1][x+x1]=}" + f" {x+x1=}" + f" {y+y1=}", file=sys.stderr, flush=True)
    if mapa[y+y1][x+x1] == "$":
        print(direction)
    elif mapa[y+y1][x+x1] == " ":
        print(direction)
        bender_pos[0] += x1
        bender_pos[1] += y1
        currentState[0] = space_state
        look_for_directions(space_state)
    elif mapa[y+y1][x+x1] == "E" or mapa[y+y1][x+x1] == "N" or mapa[y+y1][x+x1] == "W" or mapa[y+y1][x+x1] == "S":
        print(direction)
        bender_pos[0] += x1
        bender_pos[1] += y1
        direction2, x1, y1 = f_path_modifiers(mapa[y+y1][x+x1])
        currentState[0] = path_modifiers
        look_for_directions(path_modifiers)
    elif mapa[y+y1][x+x1] == "#" or mapa[y+y1][x+x1] == "X":
        if mapa[y+y1][x+x1] == "X" and states[1] == True:
            print(direction)
        else:
            direction2, x1, y1 = find_path(1)
            print(direction2)
        bender_pos[0] += x1
        bender_pos[1] += y1
        currentState[0] = obstacles_state
        look_for_directions(obstacles_state)
    elif mapa[y+y1][x+x1] == "I":
        print(direction)
        bender_pos[0] += x1
        bender_pos[1] += y1
        states[0] = True if states[0] == False else False
        currentState[0] = circuit_inverters
        look_for_directions(circuit_inverters)
    elif mapa[y+y1][x+x1] == "B":
        print(direction)
        bender_pos[0] += x1
        bender_pos[1] += y1
        states[1] = True if states[1] == False else False
        currentState[0] = beer_state
        look_for_directions(beer_state)

look_for_directions()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
