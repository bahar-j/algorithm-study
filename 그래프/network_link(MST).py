# https://www.acmicpc.net/problem/1922
# 방문 확인은 실제로 방문했을 때 해야함
# 새로 방문하는 노드에 대해서만 인접 정점 힙에 넣어주기

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
G = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append([c, b])
    G[b].append([c, a])

min_heap = []
heapq.heappush(min_heap, [0, 1])
answer = 0
visited = [False]*(N+1)

while min_heap:
    weight, node = heapq.heappop(min_heap)

    if not visited[node]:
        answer += weight
        visited[node] = True

        adjacents = G[node]
        for a in adjacents:
            if not visited[a[1]]:
                heapq.heappush(min_heap, a)

    if visited.count(True) == N:
        break

print(answer)
