# https://www.acmicpc.net/problem/11725
import sys

sys.setrecursionlimit(10**6)

def dfs(now):
    children = tree[now]

    for child in children:
        if parent[child] == 0:
            parent[child] = now
            dfs(child)


input = sys.stdin.readline
N = int(input())
tree = {i: [] for i in range(1, N+1)}
parent = [0] * (N+1)
parent[1] = -1

for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

dfs(1)

for i in range(2, len(parent)):
    print(parent[i])

