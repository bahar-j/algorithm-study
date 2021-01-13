# https://www.acmicpc.net/problem/10971
from sys import stdin
from math import inf

def traverse(before, now, cost):
    global min_cost, visited
    cost += G[before][now]
    visited[now] = True

    if (False not in visited) and (G[now][0] != 0):
        cost += G[now][0]
        min_cost = min(min_cost, cost)

    for next_city in range(N):
        if (not visited[next_city]) and G[now][next_city] != 0:
            traverse(now, next_city, cost)
            visited[next_city] = False

N = int(input())
G = []

for _ in range(N):
    G.append(list(map(int, stdin.readline().split())))


min_cost = inf
for next_city in range(1, N):
    visited = [False] * N
    visited[0] = True
    if G[0][next_city] != 0:
        traverse(0, next_city, 0)

print(min_cost)
