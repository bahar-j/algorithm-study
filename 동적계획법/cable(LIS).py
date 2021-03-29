# https://www.acmicpc.net/problem/2565
# LIS

import sys

input = sys.stdin.readline
N = int(input())
G = [[0, 0]]
DP = [0] * (N+1)

for _ in range(N):
    G.append(list(map(int, input().split())))

G.sort()

for i in range(1, len(G)):
    now = G[i][1]
    tmp = []
    for j in range(i-1, -1, -1):
        if G[j][1] < now:
            tmp.append(DP[j])
    DP[i] = max(tmp) + 1

print(N-max(DP))
