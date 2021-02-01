# https://www.acmicpc.net/problem/1753

from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
G = {i: [] for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    G[u].append([v, w])


dist = [float('inf')] * (V+1)  # K로부터의 거리
dist[K] = 0
queue = list()
queue.append([dist[K], K])  # K까지의 거리, 정점 이름 (min-heap)
while queue:
    u = heapq.heappop(queue)[1]
    for v, w in G[u]:  # u의 모든 인접 정점에 대해서, 해당 정점에서 u를 거쳐서 K까지 갈 때의 거리를 relax
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(queue, [dist[v], v]) # 이미 relax한 정점 queue에 넣음
    # print(queue)
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])

