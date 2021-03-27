# https://www.acmicpc.net/problem/1309

import sys

input = sys.stdin.readline
N = int(input())
DP = [[0]*3 for _ in range(N)] # x, 왼쪽, 오른쪽
DP[0] = [1, 1, 1]

for i in range(1, N):
    DP[i][0] = sum(DP[i-1]) % 9901
    DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % 9901
    DP[i][2] = (DP[i-1][0] + DP[i-1][1]) % 9901

print(sum(DP[-1]) % 9901)