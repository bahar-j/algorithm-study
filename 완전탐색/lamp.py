# https://www.acmicpc.net/problem/1034
import sys
from collections import defaultdict
# 무조건 행의 상태가 같아야만 함께 켜질 수 있다.
# 1. 한 행에 꺼져있는 램프의 갯수가 K와 같은 경우
# 2. 한 행에 꺼져있는 램프의 갯수가 K보다 작으면, K-꺼진 램프의 수가 2의 배수여야 한다.

input = sys.stdin.readline

N, M = map(int, input().split())
lamps = [input().rstrip() for _ in range(N)]
lamp_pattern = defaultdict(int)
K = int(input())

for i in range(N):
    lamp = lamps[i]
    zero_count = lamp.count('0')
    if zero_count == K:
        lamp_pattern[lamp] += 1
    elif zero_count < K and not (K - zero_count) % 2:
        lamp_pattern[lamp] += 1

if not lamp_pattern.values():
    print(0)
else:
    print(max(lamp_pattern.values()))




