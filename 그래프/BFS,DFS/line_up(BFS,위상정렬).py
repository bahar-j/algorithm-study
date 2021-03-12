# https://www.acmicpc.net/problem/2252
# 위상 정렬: 사이클이 없고 방향만 존재하는 그래프에서 정점을 순서대로 나열
# 방법
# 진입 루트(indegree)가 없는 정점을 먼저 큐에 넣고
# 최상위 노드는 바로 줄세우고,
# 자식 노드는 해당 노드에서 끊어내고(indegree-1) 더 이상 부모 노드가 없을 때 줄세운다.

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
queue = deque([])
answer = []

for _ in range(M):
    parent, child = map(int, input().split())
    G[parent].append(child)
    indegree[child] += 1 # 부모의 갯수

for i in range(1, N+1):
    if not indegree[i]:
        queue.append(i) # 루트 노드

while queue:
    node = queue.popleft()
    answer.append(node)
    for child in G[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
            queue.append(child)

print(*answer)