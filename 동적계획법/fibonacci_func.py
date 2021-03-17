# https://www.acmicpc.net/problem/1003

# 4 -> 3 + 2
# 3 -> 2 + 1
# 2 -> 1 + 0
# 1 -> print(1)
# 0 -> print(0)

import sys

input = sys.stdin.readline
T = int(input())
nums = []
DP = [0] * 41
DP[0] = [1, 0]
DP[1] = [0, 1]

for _ in range(T):
    nums.append(int(input()))

for i in range(2, max(nums)+1):
    zero = 0
    one = 0
    for j in range(1, 3):
        zero += DP[i-j][0]
        one += DP[i-j][1]
    DP[i] = [zero, one]

for n in nums:
    print(*DP[n])