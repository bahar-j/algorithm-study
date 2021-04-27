# https://www.acmicpc.net/problem/2805
# 이분 탐색 기준 == 자를 나무의 길이
# 이분 탐색 max 정할 때 주의하기 !

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)
answer = 0

while left <= right:
    mid = (left+right)//2
    bring = sum([(tree - mid if tree > mid else 0) for tree in trees])
    if bring > M: # 너무 낮은 높이에서 자름
        left = mid + 1
        answer = mid
    elif bring < M:
        right = mid - 1
    else:
        answer = mid
        break

print(answer)
