import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count_y = 1
start_of_area = 0
end_of_area = 0
last_y = land_y = last_x = land_x = continuaba = 0

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    last_y = land_y
    last_x = land_x
    land_x, land_y = [int(j) for j in input().split()]
    #calculating start and end of area
    if land_y ==  last_y:
        count_y += 1
        if count_y == 2:
            start_of_area = last_x
    elif count_y >= 2 and continuaba == 0:
        end_of_area = last_x
        floor = last_y
        continuaba = 1
        if end_of_area - start_of_area < 999:
            start_of_area = end_of_area = count_y = floor = continuaba = 0

print(f"{start_of_area = }", file=sys.stderr, flush=True)
print(f"{end_of_area=}", file=sys.stderr, flush=True)
middle_area = (start_of_area + end_of_area)/2
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    #seconds_to_floor_impact with the floor
    seconds_to_floor_impact = (floor - y)/((v_speed - 38)/2)
    print(f"{seconds_to_floor_impact=}", file=sys.stderr, flush=True)
    if x < start_of_area -100:
        min_h_speed = (start_of_area + 200 - x)/seconds_to_floor_impact
        max_h_speed = (end_of_area - 200 - x)/seconds_to_floor_impact
        if h_speed < min_h_speed:
            angle = -45
            flame = 4
        elif h_speed > max_h_speed:
            angle = 45
            flame = 4
        elif v_speed < -38:
            angle = 0
            flame = 4
        else:
            flame = 0

    elif x > end_of_area + 100:
        min_h_speed = (end_of_area - 200 - x)/seconds_to_floor_impact
        max_h_speed = (start_of_area + 200 - x)/seconds_to_floor_impact
        print(f"{max_h_speed=}", file=sys.stderr, flush=True)
        if h_speed > min_h_speed:
            angle = 45
            flame = 4
        elif h_speed < max_h_speed:
            angle = -45
            flame = 4
        elif v_speed < -38:
            angle = 0
            flame = 4
        else:
            flame = 0
        #I want to reduce h speed to less than 20 
    else:
        min_h_speed = (middle_area - x)/seconds_to_floor_impact
        if abs(h_speed) < 20:
            angle = 0
        elif h_speed >= 20:
            angle = 22
        elif h_speed <= -20:
            angle = -22
        if v_speed < -35:
            flame = 4
        else:
            flame = 0

    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(angle, flame)
