# https://www.acmicpc.net/problem/14501

import sys

input = sys.stdin.readline
N = int(input())
G = [[0, 0]]
max_val = 0
DP = [0]*(N+1)

for _ in range(N):
    G.append(list(map(int, input().split())))

DP.append(0)

for i in range(N, 0, -1):
    if i + G[i][0] <= N:
        DP[i] = max(DP[i+G[i][0]] + G[i][1], DP[i+1])
    else:
        if i + G[i][0] == N+1:
            DP[i] = max(G[i][1], DP[i+1])
        else:
            DP[i] = max(0, DP[i+1])

print(max(DP))
