# https://www.acmicpc.net/problem/1949
import sys
from collections import defaultdict
# 트리 DP

sys.setrecursionlimit(10**6)

def dfs(now):
    visited[now] = True
    children = TREE[now]

    for child in children:
        if not visited[child]:
            dfs(child)
            # 끝까지 들어간 후 나오면서 계산
            DP[now-1][0] += max(DP[child-1][0], DP[child-1][1])
            DP[now-1][1] += DP[child-1][0]

input = sys.stdin.readline
N = int(input())
people_per_village = list(map(int, input().split()))
TREE = defaultdict(list)
visited = [False] * (N+1)
DP = [[0, people_per_village[i]] for i in range(N)] # 우수 마을이 아닌 경우, 우수 마을인 경우

for _ in range(N-1):
    from_, to_ = map(int, input().split())
    TREE[from_].append(to_)
    TREE[to_].append(from_)

dfs(1)
print(max(DP[0][0], DP[0][1]))


