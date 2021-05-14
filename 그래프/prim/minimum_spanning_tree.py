# https://www.acmicpc.net/problem/1197
# 최소 신장 트리 (모든 정점을 연결하는 간선들의 합 중 사이클이 생기지 않으면서 가장 작은 값)
# 크루스칼 알고리즘(가중치가 작은 간선부터) - 간선이 적은 경우 유리
# 프림 알고리즘(임의의 시작점에 대해 연결된 정점들 중 가중치가 작은 것부터) - 간선이 많은 경우 유리

import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
G = {i: [] for i in range(1, V+1)}
visited = [False] * (V+1)
min_heap = []
answer = 0

def prim(now):
    global V, G, visited, min_heap, answer

    visited[now] = True
    adjacents = G[now]
    for adjacent in adjacents:
        heapq.heappush(min_heap, adjacent)

    while min_heap:
        if visited.count(True) == V:
            return

        weight, vertex = heapq.heappop(min_heap)

        if not visited[vertex]:
            answer += weight
            visited[vertex] = True

            adjacents = G[vertex]
            for adjacent in adjacents:
                heapq.heappush(min_heap, adjacent)


def main():
    global G, visited, min_heap, answer

    for _ in range(E):
        start, end, weight = map(int, input().split())
        G[start].append([weight, end])
        G[end].append([weight, start])

    prim(1)
    print(answer)

main()


