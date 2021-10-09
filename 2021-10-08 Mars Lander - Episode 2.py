import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count_y = 1
start_of_area = 0
end_of_area = 0
last_y = land_y = last_x = land_x = continuaba = 0
surface = {}

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    last_y = land_y
    last_x = land_x
    land_x, land_y = [int(j) for j in input().split()]
    surface[i] = (land_x, land_y)
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
bloqueo = 0
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
    
    #Calculating obstacles
    obstacle = -1
    to_right = True
    if abs(h_speed) > 5:
        for i in surface:
            if x < surface[i][0] < middle_area:
                #calculating the inclination and height of the next obstacle
                m = (y - floor)/(middle_area - x)
                if ((y - floor) - m*(surface[i][0] - x)) < (surface[i][1] - floor):
                    obstacle = i
                    to_right = True
                    seconds_to_floor_impact = (surface[i][1] + 50 - y)/((v_speed - 10)/2)
                    print(f"{i=}", file=sys.stderr, flush=True)
                    print(f"{m=}", file=sys.stderr, flush=True)
                    print(f"{m*(surface[i][0] - x)=}", file=sys.stderr, flush=True)
                    print(f"{surface[i][1] - floor=}", file=sys.stderr, flush=True)
            elif x > surface[i][0] > middle_area:
                m = (y - floor)/(x - middle_area)
                if ((y - floor) - m*(x - surface[i][0])) < (surface[i][1] - floor):
                    obstacle = i
                    to_right = False
                    seconds_to_floor_impact = (surface[i][1] + 50 - y)/((v_speed - 10)/2)
    
    print(f"{seconds_to_floor_impact=}", file=sys.stderr, flush=True)
    if x < middle_area:
        min_h_speed = (start_of_area + 200 - x)/seconds_to_floor_impact
        max_h_speed = (end_of_area - 200 - x)/seconds_to_floor_impact
        if bloqueo == 1:
            prefered_angle = -5
        else:
            prefered_angle = 45 if h_speed - max_h_speed < 80 else 60
        if abs((middle_area - x)/(y - floor)) > 2:
            prefered_angle = -5
            bloqueo = 1
        if obstacle != -1: prefered_angle = 10
        if h_speed < min_h_speed:
            angle = -prefered_angle
            flame = 4
        elif h_speed > max_h_speed:
            angle = prefered_angle
            flame = 4
        elif v_speed < -33:
            flame = 4
            if seconds_to_floor_impact < 25:
                if h_speed > 18:
                    angle = prefered_angle
                elif h_speed < -18:
                    angle = -prefered_angle
                else:
                    angle = 0
            else:
                angle = 0
        else:
            flame = 0

    elif x > middle_area:
        min_h_speed = (end_of_area - 200 - x)/seconds_to_floor_impact
        max_h_speed = (start_of_area + 200 - x)/seconds_to_floor_impact
        if bloqueo == 1:
            prefered_angle = -5
        else:
            prefered_angle = 45 if h_speed - max_h_speed > -80 else 60
        if abs((middle_area - x)/(y - floor)) > 2:
            prefered_angle = -5
            bloqueo = 1
        if obstacle != -1: prefered_angle = 10
        if h_speed > min_h_speed:
            angle = prefered_angle
            flame = 4
        elif h_speed < max_h_speed:
            angle = -prefered_angle
            flame = 4
        elif v_speed < -33:
            flame = 4
            if seconds_to_floor_impact < 25:
                if h_speed > 18:
                    angle = prefered_angle
                elif h_speed < -18:
                    angle = -prefered_angle
                else:
                    angle = 0
            else:
                angle = 0
        else:
            flame = 0
        #I want to reduce h speed to less than 20 
    else:
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
    print(f"{min_h_speed=}", file=sys.stderr, flush=True)
    print(f"{max_h_speed=}", file=sys.stderr, flush=True)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(angle, flame)
