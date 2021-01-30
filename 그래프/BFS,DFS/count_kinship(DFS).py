# https://www.acmicpc.net/problem/2644

import sys
from collections import defaultdict

def dfs(now, count):
    visited[now] = True
    if now == y:
        print(count)
        sys.exit(0)
        return

    relationships = tree[now]

    for relation in relationships:
        if not visited[relation]:
            dfs(relation, count+1)


input = sys.stdin.readline
N = int(input())
x, y = map(int, input().split())
M = int(input())
tree = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    parent, child = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)

dfs(x, 0)
print(-1)