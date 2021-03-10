# https://www.acmicpc.net/problem/1967
# dfs 2번
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
G = {i : [] for i in range(1, N+1)}

for _ in range(N-1):
    s, e, w = map(int, input().split())
    G[s].append([e, w])
    G[e].append([s, w])

queue = deque([])
queue.append([1, 0])
visited = [False]*(N+1)
visited[1] = True
leafs = []

# 가장 먼 리프 노드 찾기
farthest = 1
max_dis = 0
while queue:
    now, dis = queue.popleft()
    isLeaf = True
    for e, w in G[now]:
        if not visited[e]:
            queue.append([e, dis+w])
            visited[e] = True
            isLeaf = False
    if isLeaf:
        if max_dis < dis:
            farthest = now
            max_dis = dis
        leafs.append(now)

answer = max_dis
visited = [False] * (N + 1)
queue2 = deque([])
queue2.append([farthest, 0])
visited[farthest] = True
while queue2:
    now, length = queue2.popleft()
    answer = max(answer, length)
    for e, w in G[now]:
        if not visited[e]:
            visited[e] = True
            queue2.append([e, length + w])

print(answer)

# <풀이 2> => 리프노드인지 확인해주는 과정 때문에 훨씬 오래 걸림
# answer = max_dis -> 이 방법에서는 리프 노드에서만 갱신하므로 루트랑도 꼭 비교해줘야함
# visited = [False] * (N + 1)
# queue2 = deque([])
# queue2.append([farthest, 0])
# visited[farthest] = True
# while queue2:
#     now, length = queue2.popleft()
#     for e, w in G[now]:
#         if not visited[e] and e in leafs:
#             visited[e] = True
#             answer = max(answer, length + w) -> 리프 노드에 도착했을 때 갱신
#         elif not visited[e]:
#             visited[e] = True
#             queue2.append([e, length + w])

