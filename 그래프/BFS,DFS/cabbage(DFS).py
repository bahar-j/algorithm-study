# https://www.acmicpc.net/problem/1012

import sys

sys.setrecursionlimit(10**6)

def get_group(x, y):
    G[x][y] = 2

    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < N and 0 <= new_y < M:
            if G[new_x][new_y] == 1:
                get_group(new_x, new_y)

input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

T = int(input())
for _ in range (T):
    worm = 0
    M, N, K = map(int, input().split())
    G = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        G[x][y] = 1

    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                get_group(i, j)
                worm += 1
    print(worm)