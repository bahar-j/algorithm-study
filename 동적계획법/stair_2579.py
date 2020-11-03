# https://www.acmicpc.net/problem/2579

import sys

N = int(sys.stdin.readline().strip())
score_per_stair = [int(sys.stdin.readline().strip()) for i in range(N)]

for i in range(3):
    score_per_stair.insert(0, 0)

STAIR = [0] * (N+3)

for i in range(3, N+3):
    STAIR[i] = max(STAIR[i-3]+score_per_stair[i-1], STAIR[i-2]) + score_per_stair[i]

print(STAIR[-1])