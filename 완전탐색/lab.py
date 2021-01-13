# https://www.acmicpc.net/problem/14502
from sys import stdin
from itertools import combinations
import copy

def dfs(h, w):
    new_graph[h][w] = '3'
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    if h == 1:
        directions.remove((-1, 0))
    if h == N:
        directions.remove((1, 0))
    if w == 1:
        directions.remove((0, -1))
    if w == M:
        directions.remove((0, 1))

    for direction in directions:
        if new_graph[h + direction[0]][w + direction[1]] == '0':
            dfs(h + direction[0], w + direction[1])

N, M = map(int, stdin.readline().split())
G = [[0]*(M+2)]
NUM_WALLS = 3
wall_place = []
max_count = 0
for height in range(N):
    row = [0]
    new_row = list(stdin.readline().split())
    for width in range(len(new_row)):
        if new_row[width] == '0':
            wall_place.append([height+1, width+1])
    row.extend(new_row)
    row.append(0)
    G.append(row)
G.append([0]*(M+2))
combi = list(combinations(wall_place, NUM_WALLS))

for item in combi:
    count = 0
    new_graph = copy.deepcopy(G)
    for i in range(NUM_WALLS):
        new_graph[item[i][0]][item[i][1]] = '1'
    for h in range(1, N+1):
        for w in range(1, M+1):
            if new_graph[h][w] == '2':
                dfs(h, w)
    for j in range(1, N+1):
        count += new_graph[j].count('0')
    max_count = max(max_count, count)

print(max_count)