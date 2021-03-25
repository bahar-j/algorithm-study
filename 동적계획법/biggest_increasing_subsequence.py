# https://www.acmicpc.net/problem/11055

import sys

input = sys.stdin.readline
A = int(input())
nums = list(map(int, input().split()))
DP = [0 for _ in range(A+1)]
nums.insert(0, 0)

for i in range(1, A+1):
    tmp = []
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            tmp.append(DP[j])
    DP[i] = max(tmp) + nums[i]

print(max(DP))