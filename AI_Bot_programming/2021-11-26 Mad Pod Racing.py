import sys
import math

center_x = 16000/2
center_y = 9000/2

boost_is_used = False

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #print(f"{next_checkpoint_x=}", file=sys.stderr, flush=True)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    speed = 100
    if not boost_is_used and next_checkpoint_dist > 8000 and abs(next_checkpoint_angle) < 20:
        speed = "BOOST"
        boost_is_used = True
    elif next_checkpoint_dist < 250:
        speed = 50
    elif abs(next_checkpoint_angle) > 90:
        speed = 2
    
    closeness = 0

    x0 = next_checkpoint_x - center_x
    y0 = next_checkpoint_y - center_y
    m = y0/x0
    if y0 > 0:
        y1 = y - closeness/math.sqrt((pow(m, 2) + 1))
    else:
        y1 = y0 + closeness/math.sqrt((pow(m, 2) + 1))

    x1 = y1/m

    print(f"{x=} {y=}", file=sys.stderr, flush=True)

    xm=x
    ym=y
    print(str(int(next_checkpoint_x)) + " " + str(int(next_checkpoint_y)) + " " + str(speed))
    #Debug
    #print(f"{speed=}", file=sys.stderr, flush=True)
