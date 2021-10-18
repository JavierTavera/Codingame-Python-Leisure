n = int(input())  # the number of relationships of influence
nodes = {}
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if not x in nodes.keys(): nodes[x] = [y]
    else: nodes[x].append(y)

initial_q = []
initial_q.append(0)

def count_nodes(nod, q = 2):
    for i in range(len(nod)):
        if nod[i] in nodes:
            count_nodes(nodes[nod[i]], q+1)
        else:
            if q > initial_q[0]: initial_q[0] = q

for node in nodes:
    if node in nodes: count_nodes(nodes[node])

print(initial_q[0])
