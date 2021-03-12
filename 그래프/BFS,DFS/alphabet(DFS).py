# https://www.acmicpc.net/problem/1987
# pypy만 통과

import sys
from collections import deque


input = sys.stdin.readline
R, C = map(int, input().split())
G = []
for _ in range(R):
    G.append(list(input().rstrip()))
directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
answer = 0

def dfs(x, y, path):
    global answer

    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < R and 0 <= new_y < C:
            if G[new_x][new_y] not in path:
                dfs(new_x, new_y, path+G[new_x][new_y])
            else:
                answer = max(answer, len(path))

def main():
    dfs(0, 0, G[0][0])

main()
print(answer)