# https://www.acmicpc.net/problem/1916

import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
G = {i: [] for i in range(1, N+1)}

for _ in range(M):
    start_, end_, weight = map(int, input().split())
    G[start_].append([end_, weight])

print(G)

d_start, d_end = map(int, input().split())
dist = [float('inf')] * (N+1)
dist[d_start] = 0
queue = []
queue.append([dist[d_start], d_start])
while queue:
    u = heapq.heappop(queue)[1]
    for v, w in G[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(queue, [dist[v], v])

print(dist[d_end])