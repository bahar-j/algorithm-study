# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

def dfs(now):
    global answer

    adjacents = graph[now]
    visited[now] = True
    answer.append(now)

    for a in adjacents:
        if not visited[a]:
            dfs(a)

def bfs(now):
    queue = deque([now])
    visited = [False] * (N+1)
    visited[now] = True

    while queue:
        next = deque.popleft(queue)
        answer.append(next)
        adjacents = graph[next]
        for a in adjacents:
            if not visited[a]:
                queue.append(a)
                visited[a] = True


input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}
answer = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
dfs(V)
print(*answer)
answer.clear()
bfs(V)
print(*answer)