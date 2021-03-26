# https://www.acmicpc.net/problem/5014

import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
directions = (U, -D)

queue = deque([])
queue.append([S, 0])
visited = [False] * (F+1)
visited[S] = True

while queue:
    now, cnt = queue.popleft()
    if now == G:
        print(cnt)
        exit(0)
    for d in directions:
        new_now = now + d
        if 1 <= new_now <= F:
            if not visited[new_now]:
                visited[new_now] = True
                queue.append([new_now, cnt+1])

print("use the stairs")