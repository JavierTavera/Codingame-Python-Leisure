import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_floors = {}
elevator_poss = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_floors[i] = elevator_floor
    elevator_poss[i] = elevator_pos

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    if clone_floor == -1:
        print("WAIT")
        continue

    if exit_floor == clone_floor:
        elev_pos = exit_pos
    elif nb_elevators != 0:
        print(clone_floor, file=sys.stderr, flush=True)
        print(elevator_floors, file=sys.stderr, flush=True)
        keys = [k for k, v in elevator_floors.items() if v == clone_floor]
        print(keys, file=sys.stderr, flush=True)
        elev_pos = elevator_poss[keys[0]]

    if clone_pos == elev_pos:
        print("WAIT")
    elif clone_pos < elev_pos:
        if direction == "RIGHT":
            print("WAIT")
        else:
            print("BLOCK")
    else:
        if direction == "RIGHT":
            print("BLOCK")
        else:
            print("WAIT")

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # action: WAIT or BLOCK
    #print("WAIT")
