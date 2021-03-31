# https://www.acmicpc.net/problem/2225

# DP[i][j] = DP[i][j-1] + DP[i-1][j]

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
DP = [[0]*(N+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        if i == 1:
            DP[i][j] = 1
            continue
        elif j == 1:
            DP[i][j] = i
            continue
        DP[i][j] = DP[i][j-1] + DP[i-1][j]

print(DP[-1][-1] % 1_000_000_000)