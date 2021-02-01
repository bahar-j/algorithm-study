# https://www.acmicpc.net/problem/1261
import sys
from collections import deque

def bfs(x, y):
    broken = 0
    queue = deque([[x, y, broken]])

    while queue:
        a, b, broken = queue.popleft()
        if a == M-1 and b == N-1:
            print(broken)
            return
        for d in directions:
            new_a = a + d[0]
            new_b = b + d[1]
            if 0 <= new_a < M and 0 <= new_b < N:
                if not visited[new_a][new_b]:
                    if map[new_a][new_b] == '1':
                        queue.append([new_a, new_b, broken+1])
                        visited[new_a][new_b] = True
                    elif map[new_a][new_b] == '0':
                        queue.appendleft([new_a, new_b, broken])
                        visited[new_a][new_b] = True

input = sys.stdin.readline
N, M = map(int, input().split())
map = []
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

for _ in range(M):
    map.append(list(input().rstrip()))

visited = [[False] * N for _ in range(M)]
visited[0][0] = True
bfs(0, 0)