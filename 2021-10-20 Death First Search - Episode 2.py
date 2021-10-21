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
possible_routes = []
possible_nodes = []
first_node = []
#steps_to_gateway = {ei[i]:-1 for i in range(e)}
doNotVisitAgain = []

def f_steps_to_gateway(a_node):
    nextNode = [a_node]
    tempNodes = []
    #steps = 0
    while True:
        print(f"{nextNode = }", file=sys.stderr, flush=True)
        tempNodes.clear()
        possible_routes.clear()
        for nod in nextNode:
            doNotVisitAgain.append(nod)
            print(f"{doNotVisitAgain = }", file=sys.stderr, flush=True)
            for nod3 in link[nod]:
                print(f"{nod3 = }", file=sys.stderr, flush=True)
                print(f"{nod = }", file=sys.stderr, flush=True)
                print(f"{sever_link[nod3] = }", file=sys.stderr, flush=True)
                if nod in ei and not nod in sever_link[nod3]:
                    sever_link[nod3] = sever_link[nod3] + [nod]
                    sever_link[nod] = sever_link[nod] + [nod3]
                    print(nod, nod3, file=sys.stderr, flush=True)
                    doNotVisitAgain.clear()
                    # in here, nod would be the gateway
                    #possible_routes.append([nod3, nod])
                    return str(nod) + " " + str(nod3)
                else:
                    for knod in ei:
                        if nod in link[knod] and not nod in sever_link[knod] and knod  == nod3: # in here, knod would be the gateway
                            print(nod, knod, file=sys.stderr, flush=True)
                            doNotVisitAgain.clear()
                            possible_routes.append([nod, knod])
                            print(f"{possible_routes = }", file=sys.stderr, flush=True)
                            #return str(nod) + " " + str(knod)
        print(f"{possible_routes = }", file=sys.stderr, flush=True)
        if len(possible_routes) > 0:
            first_node.clear()
            for routes in possible_routes:
                print(f"{routes = }", file=sys.stderr, flush=True)
                print(f"{first_node = }", file=sys.stderr, flush=True)
                if not routes[0] in first_node:
                    possible_nodes.append(routes)
                    first_node.append(routes[0])
                else:
                    sever_link[routes[0]] = sever_link[routes[0]] + [routes[1]]
                    sever_link[routes[1]] = sever_link[routes[1]] + [routes[0]]
                    return str(routes[0]) + " " + str(routes[1])
            sever_link[possible_routes[0][0]] = sever_link[possible_routes[0][0]] + [possible_routes[0][1]]
            sever_link[possible_routes[0][1]] = sever_link[possible_routes[0][1]] + [possible_routes[0][0]]
            return str(possible_routes[0][0]) + " " + str(possible_routes[0][1])

        for nod in nextNode:
            for nod2 in link[nod]:
                if not nod2 in doNotVisitAgain and not nod2 in nextNode:
                    print(f"{nod2 = }", file=sys.stderr, flush=True)
                    tempNodes.append(nod2)
            nextNode.clear()
            nextNode = [-1] + tempNodes
            nextNode.remove(-1)

#ei = []
#for i in range(e):
#    ei.append(int(input()))  # the index of a gateway node

sever_link = {i:[] for i in range(n)}
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    print(f"{si = }", file=sys.stderr, flush=True)

    print(f_steps_to_gateway(si))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
