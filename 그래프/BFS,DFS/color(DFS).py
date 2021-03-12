# https://www.acmicpc.net/problem/10026

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
G = []
for _ in range(N):
    G.append(list(input().rstrip()))
answer = {'G': 0, 'not_G': 0}
directions = ((1,0), (0,1), (-1, 0), (0, -1))

def dfs(x, y, visited):
    color = G[x][y]
    visited[x][y] = True
    if color == 'R':
        G[x][y] = 'G'

    for d in directions:
        new_x = d[0] + x
        new_y = d[1] + y
        if 0 <= new_x < N and 0 <= new_y < N:
            if not visited[new_x][new_y] and G[new_x][new_y] == color:
                dfs(new_x, new_y, visited)


def main():
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited)
                answer['G'] += 1

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited)
                answer['not_G'] += 1


main()
print(*answer.values())