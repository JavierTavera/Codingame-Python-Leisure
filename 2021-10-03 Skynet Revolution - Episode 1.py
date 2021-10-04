import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
links = {}
linksChecked = []
ei = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    if n1 in links.keys():
        if not n2 in links[n1]:
            links[n1].append(n2)
    else:
        links[n1] = [n2]

    if n2 in links.keys():
        if not n1 in links[n2]:
            links[n2].append(n1)
    else:
        links[n2] = [n1]
    
for i in range(e):
    ei.append([int(input()), 0])  # the index of a gateway node

def gateway_access(sk, gw, currentNode, i, lastNode = -1):
    global minN
    print(sk, gw, currentNode, file=sys.stderr, flush=True)
    if sk in links[currentNode]:
        print("retorna", file=sys.stderr, flush=True)
        #pase = False
        if i == 0: minN = currentNode
        elif ei[i][1] < ei[i - 1][1]: minN = currentNode
        return sk, currentNode
    else:
        linksChecked.append((lastNode, currentNode))
        ##linksChecked.append((currentNode, lastNode))
        for j in range(len(links[currentNode])):
            if not (currentNode, links[currentNode][j]) in linksChecked and links[currentNode][j] != lastNode:

                ei[i][1] += 1
                print(str(j) + " " + str(ei[i][1]), file=sys.stderr, flush=True)
                return gateway_access(sk, gw, links[currentNode][j], i, currentNode)


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    ##pase = True
    minN = -1
    
    for i in range(len(ei)): ei[i][1] = 0

    for i in range(len(ei)):
        p1, p2 = gateway_access(si, ei[i][0], ei[i][0], i)
        linksChecked.clear()
        print(str(p1) + " " + str(p2), file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(str(p1) + " " + str(minN))
