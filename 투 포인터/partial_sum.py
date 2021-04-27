# https://www.acmicpc.net/problem/1806
# 무조건 차례로 진행 x
# 구하려는 값보다 크면 left + 1
# 작으면 right + 1
# 작지만 right 범위를 벗어난다면 break

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
answer = float('inf')

sum_nums = [0] * (N+1)
for i in range(1, N+1):
    sum_nums[i] = sum_nums[i-1] + nums[i-1]

while True:
    if sum_nums[right] - sum_nums[left] >= S:
        answer = min(answer, right-left)
        left += 1
    else:
        if right != N:
            right += 1
        else:
            break

if answer == float('inf'):
    print(0)
else:
    print(answer)