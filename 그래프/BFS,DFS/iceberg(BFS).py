# https://www.acmicpc.net/problem/2573
# 덩어리 찾는 문제 BFS로도 가능

import sys

sys.setrecursionlimit(10**4)

def melt(x, y):
    water = 0
    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < N and 0 <= new_y < M:
            if G[new_x][new_y] == 0 or G[new_x][new_y] == '*'*time:
                water += 1
    return water

def dfs(x, y):
    visited[x][y] = True

    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < N and 0 <= new_y < M:
            if G[new_x][new_y] != 0 and not visited[new_x][new_y] and G[new_x][new_y] != '*'*time:
                dfs(new_x, new_y)

input = sys.stdin.readline
N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range (N)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
group = 0
time = 0

while True:
    group = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if G[i][j] == '*'*time:
                G[i][j] = 0
            if G[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                group += 1
            if G[i][j] != 0:
                melted = melt(i, j)
                if (G[i][j] - melted) > 0:
                    G[i][j] -= melted
                else:
                    G[i][j] = '*'*(time+1)

    if group >= 2:
        break
    if group == 0:
        break

    time += 1

print(0) if group == 0 else print(time)