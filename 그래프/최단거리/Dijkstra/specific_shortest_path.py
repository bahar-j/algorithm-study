# https://www.acmicpc.net/problem/1504

import sys
import heapq

def dijkstra(start):
    dis = [float('inf')] * (N + 1)
    dis[start] = 0
    queue = []
    queue.append([0, start])

    while queue:
        now = heapq.heappop(queue)[1]

        for w, v in G[now]:
            if dis[v] > dis[now] + w:
                dis[v] = dis[now] + w
                heapq.heappush(queue, [dis[v], v])
    return dis

input = sys.stdin.readline
N, E = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
answer = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append([c, b])
    G[b].append([c, a])

x, y = map(int, input().split())


dis_x = dijkstra(x)
dis_y = dijkstra(y)
answer = min(dis_x[1] + dis_x[y] + dis_y[N], dis_y[1] + dis_x[N] + dis_x[y])

if answer == float('inf'):
    print(-1)
else:
    print(answer)

