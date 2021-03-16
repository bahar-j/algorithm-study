# https://www.acmicpc.net/problem/16234

import sys
from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    union = [[a, b]]

    while queue:
        x, y = queue.popleft()
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_x][new_y]:
                    if L <= abs(G[x][y] - G[new_x][new_y]) <= R:
                        union.append([new_x, new_y])
                        queue.append([new_x, new_y])
                        visited[new_x][new_y] = True
    return union

def update(union):
    total = 0
    for u in union:
        total += G[u[0]][u[1]]
    num = total // len(union)
    for u in union:
        G[u[0]][u[1]] = num

input = sys.stdin.readline

N, L, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
answer = 0

while True:
    visited = [[False]*N for _ in range(N)]
    changed = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                union = bfs(i, j)
                if len(union) > 1:
                    update(union)
                    changed = True
    if not changed:
        break
    answer += 1

print(answer)