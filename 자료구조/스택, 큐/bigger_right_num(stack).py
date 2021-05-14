# https://www.acmicpc.net/problem/17298

import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
answer = [-1] * N
stack = []
stack.append(0)

i = 0
for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*answer)