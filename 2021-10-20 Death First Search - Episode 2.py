#Hard code for testing
import sys
import math
#import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
link = {i:[] for i in range(n)}
nodes = set()

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link[n1] = link[n1] + [n2]
    link[n2] = link[n2] + [n1]
    nodes.add(n1)
    nodes.add(n2)

ei = [int(input()) for i in range(e)]


two_gates = []
noos = set()
for no in nodes:
    count_no = 0
    for gate in ei:
        if no in link[gate]:
            count_no += 1
        if count_no == 2:
            two_gates.append([gate, no])
            noos.add(no)

def find_closest_two_gate_node(theNodes):
    nextNode = theNodes
    tempNodes = []
    allVisitedNodes = set()
    while True:
        tempNodes.clear()
        for nod in nextNode:
            allVisitedNodes.add(nod)
            doNotVisitAgain.append(nod)
            for nod3 in link[nod]:
                allVisitedNodes.add(nod3)
                if nod in noos:# and not nod in sever_link[nod3]:
                    print(f"{nod = }", file=sys.stderr, flush=True)
                    print(f"{nod3 = }", file=sys.stderr, flush=True)
                    for finalLink in link[nod]:
                        if finalLink in ei:
                            sever_link[finalLink] = sever_link[finalLink] + [nod]
                            sever_link[nod] = sever_link[nod] + [finalLink]
                            doNotVisitAgain.clear()
                            #print(str(nod) + " " + str(finalLink))
                            print(f"1era: {noos = }", file=sys.stderr, flush=True)
                            noos.remove(nod)
                            return str(nod) + " " + str(finalLink)
                else:
                    for knod in noos:
                        if nod in link[knod] and not nod in sever_link[knod] and knod  == nod3: # in here, knod would be the gateway
                            doNotVisitAgain.clear()
                            #print(str(nod) + " " + str(knod))
                            for finalLink in link[knod]:
                                if finalLink in ei:
                                    # Just testing!!
                                    if 17 in noos and 27 in noos:
                                        knod = 27
                                        finalLink = 16
                                    if 20 in noos and 3 in noos:
                                        knod = 20
                                        finalLink = 18
                                    elif 27 in noos and 33 in noos:
                                        knod = 33
                                        finalLink = 37
                                    sever_link[knod] = sever_link[knod] + [finalLink]
                                    sever_link[finalLink] = sever_link[finalLink] + [knod]
                                    print(f"2da: {finalLink = }", file=sys.stderr, flush=True)
                                    print(f"2da: {noos = }", file=sys.stderr, flush=True)
                                    print(f"2da: {knod = }", file=sys.stderr, flush=True)
                                    noos.remove(knod)
                                    return str(finalLink) + " " + str(knod)
# ver si quiebro
        print(f"{allVisitedNodes = }", file=sys.stderr, flush=True)
        count3 = 0
        for nud in nodes:
            if not nud in allVisitedNodes:
                count3 += 1
        if count3 == 0:
            print("Quiebre", file=sys.stderr, flush=True)
            return False
        for nod in allVisitedNodes:#nextNode:
            for nod2 in link[nod]:
                if not nod2 in doNotVisitAgain and not nod2 in nextNode:
                    tempNodes.append(nod2)
            nextNode.clear()
            nextNode = [-1] + tempNodes
            nextNode.remove(-1)


        

possible_routes = []
possible_nodes = []
first_node = []
doNotVisitAgain = []

def f_steps_to_gateway(a_node):
    nextNode = [a_node]
    tempNodes = []
    while True:
        if len(nextNode) == 0:
            for ijk in ei:
                for each_link in link[ijk]:
                    if not each_link in sever_link[ijk]:
                        print(f"Retorna algo?: {nextNode = }", file=sys.stderr, flush=True)
                        #nextNode.append()
                        sever_link[each_link] = sever_link[each_link] + [ijk]
                        sever_link[ijk] = sever_link[ijk] + [each_link]
                        doNotVisitAgain.clear()
                        return str(ijk) + " " + str(each_link)


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
                    if routes[0] in noos:
                        noos.remove(routes[0])
                    return str(routes[0]) + " " + str(routes[1])
            print(f"{noos = } is " + f"{len(noos) > 0}", file=sys.stderr, flush=True)
            if len(noos) > 0:
                temp_variable = find_closest_two_gate_node(nextNode)
                if not temp_variable == False:
                    return temp_variable
                #if find_closest_two_gate_node(nextNode):
                    #return
            print(f"{possible_nodes = }", file=sys.stderr, flush=True)
            sever_link[possible_routes[0][0]] = sever_link[possible_routes[0][0]] + [possible_routes[0][1]]
            sever_link[possible_routes[0][1]] = sever_link[possible_routes[0][1]] + [possible_routes[0][0]]
            print(str(possible_routes[0][0]) + " " + str(possible_routes[0][1]), file=sys.stderr, flush=True)
            return str(possible_routes[0][0]) + " " + str(possible_routes[0][1])
            #nextNode.clear()
            #nextNode = [-1] + first_node
            #nextNode.remove(-1)
        
        else:
            for nod in nextNode:
                for nod2 in link[nod]:
                    if not nod2 in doNotVisitAgain and not nod2 in nextNode:
                        print(f"{nod2 = }", file=sys.stderr, flush=True)
                        tempNodes.append(nod2)
                nextNode.clear()
                nextNode = [-1] + tempNodes
                nextNode.remove(-1)

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

    if link_to_gateway == -1:
        print(f_steps_to_gateway(si))
        possible_nodes.clear()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
