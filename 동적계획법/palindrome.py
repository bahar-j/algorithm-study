# https://www.acmicpc.net/problem/10942

import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
DP = [[0] * N for _ in range(N)]

# 길이가 1
for i in range(N):
    DP[i][i] = 1

# 길이가 2
for i in range(N-1):
    if nums[i] == nums[i+1]:
        DP[i][i+1] = 1

# 길이가 3 이상
for j in range(2, N):
    for i in range(N-j):
        # 끝이 같고 그 사이의 수가 이미 팰린드롬이면
        if nums[i] == nums[i+j] and DP[i+1][i+j-1] == 1:
            DP[i][i+j] = 1

M = int(input())
for _ in range(M):
    start_, end_ = map(int, input().split())
    print(DP[start_-1][end_-1])