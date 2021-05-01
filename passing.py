# https://www.acmicpc.net/problem/2002

import sys
from collections import defaultdict

input = sys.stdin.readline
cars = defaultdict(int)
answer = 0
out = [0]

N = int(input())
visited = [False]*(N+1)
for i in range(1, N+1):
    name = input()
    cars[name] = i

for j in range(1, N+1):
    out.append(cars[input()])

now = 1
for idx in range(1, N+1):
    visited[out[idx]] = True
    if out[idx] != now:
        answer += 1
    else:
        while visited[now]:
            now += 1
            if now >= N:
                break

print(answer)