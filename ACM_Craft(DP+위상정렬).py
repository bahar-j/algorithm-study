# https://www.acmicpc.net/problem/1005

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    tree = {i: [] for i in range(1, N+1)}
    indegree = [0] * (N+1)
    DP = [0] * (N + 1)

    for _ in range(K):
        parent, child = map(int, input().split())
        tree[parent].append(child)
        indegree[child] += 1

    queue = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            DP[i] = D[i]

    dest = int(input())

    while queue:
        now = queue.popleft()
        for c in tree[now]:
            print(now, c)
            indegree[c] -= 1
            DP[c] = max(DP[now] + D[c], DP[c])
            print(DP[c])
            if indegree[c] == 0:
                queue.append(c)
    print(DP[dest])
    print(DP)
