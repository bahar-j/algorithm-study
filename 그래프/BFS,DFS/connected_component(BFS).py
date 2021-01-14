# https://www.acmicpc.net/problem/11724

from sys import stdin

N, M = map(int, stdin.readline().split())
G = {i: [] for i in range(1, N+1)}
visited = [False for _ in range(N+1)]
visit = []
answer = 0

for _ in range(M):
    start, end = map(int, stdin.readline().split())
    G[start].append(end)
    G[end].append(start)

for i in range(1, N+1):
    if visited[i]:
        continue
    visited[i] = True
    visit.extend(G[i])
    while visit:
        dest = visit.pop()
        if not visited[dest]:
            visited[dest] = True
            visit.extend(G[dest])
    answer += 1

print(answer)



