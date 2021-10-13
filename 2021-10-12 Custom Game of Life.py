import sys

h, w, n = [int(i) for i in input().split()]
alive = input()
dead = input()
grid = {}
neighbors = {}
for i in range(h):
    grid[i] = {}
    line = input()
    for j in range(w):
        if line[j] == "O": grid[i][j] = 1
        if line[j] == ".": grid[i][j] = 0

def neighbors_turns(): # counting alive neighbors for each cell
    for i in range(h):
        neighbors[i] = {}
        for j in range(w):
            neighbors[i][j] = 0
            if i != 0: neighbors[i][j] += int(grid[i - 1][j])
            if i != 0 and j != 0: neighbors[i][j] += int(grid[i - 1][j - 1])
            if i != 0 and j != w - 1: neighbors[i][j] += int(grid[i - 1][j + 1])
            if j != 0: neighbors[i][j] += int(grid[i][j - 1])
            if j != w - 1: neighbors[i][j] += int(grid[i][j + 1])
            if i != h - 1: neighbors[i][j] += int(grid[i + 1][j])
            if i != h - 1 and j != 0: neighbors[i][j] += int(grid[i + 1][j - 1])
            if i != h - 1 and j != w - 1: neighbors[i][j] += int(grid[i + 1][j + 1])

for k in range(n):
    neighbors_turns()
    for i in range(h):
        for j in range(w):
            if dead[neighbors[i][j]] == "1" and grid[i][j] == 0:
                grid[i][j] = 1
            elif alive[neighbors[i][j]] == "0" and grid[i][j] == 1:
                grid[i][j] = 0

for i in range(h):
    st = ""
    for j in range(w):
        if grid[i][j] == 0:
            st += "."
        if grid[i][j] == 1:
            st += "O"
    print(st)

