# acmicpc.net/problem/1238
# 다익스트라: 모든 정점에서 어떤 정점까지의 최단거리
# 플로이드와샬: 모든 정점에서 모든 정점까지의 최단거리(시간복잡도 O(n^3))

# 모든 정점 -> 2
# 2 -> 모든 정점

# 플로이드와샬로도 풀 수 있지만 시간초과남
# 다익스트라 + 역방향 다익스트라

import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
G2 = {i: [] for i in range(1, N+1)}
for _ in range(M):
    start_, end_, weight = map(int, input().split())
    G[start_].append([end_, weight])
    G2[end_].append([start_, weight])

def solution():
    dis = [float('inf')] * (N+1)
    dis[X] = 0
    queue = []
    queue.append([dis[X], X])
    while queue:
        u = heapq.heappop(queue)[1]
        for v, w in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(queue, [dis[v], v])

    dis2 = [float('inf')] * (N+1)
    dis2[X] = 0
    queue = []
    queue.append([dis2[X], X])
    while queue:
        u = heapq.heappop(queue)[1]
        for v, w in G2[u]:
            if dis2[v] > dis2[u] + w:
                dis2[v] = dis2[u] + w
                heapq.heappush(queue, [dis2[v], v])

    answer = 0
    for i in range(1, N+1):
        answer = max(answer, dis[i] + dis2[i])

    return answer

print(solution())