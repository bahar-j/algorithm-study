# https://www.acmicpc.net/problem/2583
import sys

sys.setrecursionlimit(10**7)

def dfs(x, y):
    global count
    map[x][y] = 1

    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

    for direction in directions:
        new_x = x+direction[0]
        new_y = y+direction[1]
        if 0 <= new_x < M and 0 <= new_y < N:
            if map[new_x][new_y] == 0:
                count += 1
                dfs(new_x, new_y)

def paint(pos):
    x, y, x1, y1 = pos

    for j in range(y, y1):
        for i in range(x, x1):
            map[j][i] = 1

input = sys.stdin.readline
M, N, K = map(int, input().split())
box_position = []
for _ in range(K):
    box_position.append(list(map(int, input().split())))
map = [[0] * N for _ in range(M)]
answer = []
section = 0

for pos in box_position:
    paint(pos)

for i in range(M):
    for j in range(N):
        if map[i][j] == 0:
            count = 1
            dfs(i, j)
            section += 1
            answer.append(count)

answer.sort()
print(section)
print(*answer)

