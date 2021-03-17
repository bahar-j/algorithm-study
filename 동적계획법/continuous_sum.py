# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
DP = [[-1001, -1001] for _ in range(N)]
DP[0][0] = nums[0]
max_num = max(DP[0])

for i in range(1, N):
    DP[i][0] = nums[i]
    DP[i][1] = max(DP[i-1][0]+nums[i], DP[i-1][1]+nums[i])
    max_num = max(max_num, DP[i][0], DP[i][1])

print(max_num)
