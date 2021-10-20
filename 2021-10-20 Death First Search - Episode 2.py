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

ei = [int(input()) for i in range(e)]
steps_to_gateway = {ei[i]:-1 for i in range(e)}
doNotVisitAgain = []

def f_steps_to_gateway(a_node):
    nextNode = [a_node]
    tempNodes = []
    steps = 0
    while True:
        print(f"{nextNode = }", file=sys.stderr, flush=True)
        tempNodes.clear()
        for nod in nextNode:
            doNotVisitAgain.append(nod)
            for nod3 in link[nod]:
                print(f"{nod3 = }", file=sys.stderr, flush=True)
                if nod in ei and not nod in sever_link[nod3]:
                    sever_link[nod3] = sever_link[nod3] + [nod]
                    sever_link[nod] = sever_link[nod] + [nod3]
                    print(nod, nod3, file=sys.stderr, flush=True)
                    return str(nod) + " " + str(nod3)
        for nod in nextNode:
            for nod2 in link[nod]:
                if not nod2 in doNotVisitAgain and not nod2 in nextNode:
                    print(f"{nod2 = }", file=sys.stderr, flush=True)
                    tempNodes.append(nod2)
            nextNode.clear()
            nextNode = [-1] + tempNodes
            nextNode.remove(-1)
            #nextNode.remove(nod)

#ei = []
#for i in range(e):
#    ei.append(int(input()))  # the index of a gateway node

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

# sever a link to the closest gateway
# if there are 2 gateways with the same amount of steps, sever the one with more posibilities to get in

    link_to_gateway2 = True
    if link_to_gateway == -1:
        print(f_steps_to_gateway(si))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #print("3 4")

