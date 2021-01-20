# https://www.acmicpc.net/problem/11403

from sys import stdin
from collections import deque

def bfs():
    while will_visit:
        now = will_visit.popleft()

        for j in range(len(G[now])):
            if G[now][j] not in visited:
                will_visit.append(G[now][j])
                visited.append(G[now][j])

point = int(input())
G = {i: [] for i in range(1, point+1)}
answer = [[0]*point for _ in range(point)]

for i in range(point):
    points = list(stdin.readline().split())
    for j in range(len(points)):
        if points[j] == "1":
            G[i+1].append(j+1)

for i in range(1, point+1):
    will_visit = deque([])
    will_visit.append(i)
    visited = []
    bfs()
    for j in visited:
        answer[i-1][j-1] = 1

for line in answer:
    print(' '.join(map(str,line)))

