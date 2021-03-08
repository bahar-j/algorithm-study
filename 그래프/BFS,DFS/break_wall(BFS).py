# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

def BFS():
    queue = deque([])
    queue.append([0, 0, 0])
    vis[0][0][0] = 1

    while queue:
        x, y, z = queue.popleft()
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < N and 0 <= new_y < M:
                # 방문하려는 곳에 벽이 없는 경우 -> 현재 벽이 있는 없든 상관 없음
                if G[new_x][new_y] == 0 and vis[new_x][new_y][z] == -1:
                    vis[new_x][new_y][z] = vis[x][y][z] + 1
                    queue.append([new_x, new_y, z])
                # 방문하려는 곳에 벽이 있는 경우 -> 현재 벽이 없는 경우만 가능
                elif z == 0 and G[new_x][new_y] == 1 and vis[new_x][new_y][1] == -1:
                    vis[new_x][new_y][1] = vis[x][y][z] + 1
                    queue.append([new_x, new_y, 1])

input = sys.stdin.readline

N, M = map(int, input().split())
G = []
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 벽을 뚫지 않았을 때 최단 경로, 벽을 뚫었을 때 최단 경로
# -1이면 방문하기 전
vis = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    G.append(list(map(int, input().rstrip())))

BFS()

not_break_ans, break_ans = vis[-1][-1][0], vis[-1][-1][1] # n, m, 2

if not_break_ans == -1 and break_ans != -1:
    print(break_ans)
elif not_break_ans != -1 and break_ans == -1:
    print(not_break_ans)
else:
    print(min(break_ans, not_break_ans))