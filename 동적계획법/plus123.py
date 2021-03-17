# https://www.acmicpc.net/problem/9095

# 1 -> 1
# 2 -> 1 + 1 / 2
# 3 -> 1+2(2를 만드는 경우의 수) / 2+1(1을 만드는 경우의 수) / 3
# 4 -> 1 + 3(3을 만드는 경우의 수) / 2 + 2(2를 만드는 경우의 수) / 3 + 1(1을 만드는 경우의 수)
# 5 -> 1 + 4(DP(4)) / 2 + 3(DP(3))/ 3 + 2(DP(2)) / 4 + 1(x)
# 1, 2, 3의 합으로 나타내는 거니까 1, 2, 3 자체는 더 이상 분해하지 않지만
# 4의 경우는 1, 2, 3의 합으로 다시 나눠줘야함

import sys

input = sys.stdin.readline
DP = [0]*11
DP[1] = 1
DP[2] = 2
DP[3] = 4
nums = []

T = int(input())
for _ in range(T):
    nums.append(int(input()))

for i in range(4, max(nums)+1):
    DP[i] = DP[i-3]+DP[i-2]+DP[i-1]

for n in nums:
    print(DP[n])

