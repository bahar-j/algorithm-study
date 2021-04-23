# https://www.acmicpc.net/problem/2003

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
left, right = 0, 1
tmp = nums[left] # 연속합 저장

while left < N:
    print(left,right, tmp)
    if tmp == M:
        answer += 1
        tmp -= nums[left]
        left += 1

    # 아직 tmp == M인지 검사하지 않은 상태
    if right == N and tmp < M:
        break
    elif tmp < M: # 너무 짧은 경우
        tmp += nums[right]
        right += 1
    elif tmp > M: # 너무 긴 경우
        tmp -= nums[left]
        left += 1

print(answer)