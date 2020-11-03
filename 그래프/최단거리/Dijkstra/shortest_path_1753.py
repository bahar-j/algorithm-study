# https://www.acmicpc.net/problem/1753

from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
G = {i: [] for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    G[u].append([v, w])


dist = [float('inf')] * (V+1)  # 주어진 정점으로부터의 거리
dist[K] = 0
queue = list()  # min-heap
queue.append([dist[K], K])  # (weight, vertex), weight 기준 정렬
while queue:
    u = heapq.heappop(queue)[1]
    for v, w in G[u]:  # u의 모든 인접 정점 relax
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(queue, [dist[v], v])
    # print(queue)
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])

