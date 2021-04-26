# https://www.acmicpc.net/problem/1072
# 이분 탐색 기준 == (더 해야할) 게임 횟수

import sys
import math

input = sys.stdin.readline
X, Y = map(int, input().split())

Z = math.floor(Y * 100 / X)

# 99 이상이면 올릴 수 없음
if Z >= 99:
    print(-1)
else:
    left, right = 0, 1_000_000_000

    while left <= right:
        mid = (left + right)//2
        nx, ny = X + mid, Y + mid
        if math.floor(ny * 100 / nx) > Z:
            right = mid - 1
        else:
            left = mid + 1
    print(right+1)