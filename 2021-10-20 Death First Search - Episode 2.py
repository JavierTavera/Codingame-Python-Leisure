#Not yet finished

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
link = {i:[] for i in range(n)}

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link[n1] = link[n1] + [n2]
    link[n2] = link[n2] + [n1]

ei = []
for i in range(e):
    ei.append(int(input()))  # the index of a gateway node

sever_link = {i:[] for i in range(n)}
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    print(f"{si = }", file=sys.stderr, flush=True)
    link_to_gateway = -1
    for nod in link[si]:
        if nod in ei and not nod in sever_link[si]:# or si in sever_link):
            link_to_gateway = nod
            sever_link[nod] = sever_link[nod] + [si]
            sever_link[si] = sever_link[si] + [nod]
            print(nod, si)
            break

    link_to_gateway2 = True
    if link_to_gateway == -1:
        for nod in ei:
            if link_to_gateway2:
                for nod2 in link[nod]:
                    if not nod in sever_link[nod2]:# or not nod2 in sever_link:
                        link_to_gateway2 = False
                        sever_link[nod] = sever_link[nod] + [nod2]
                        sever_link[nod2] = sever_link[si] + [nod]
                        print(nod, nod2)
                        break

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #print("3 4")
