# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations
from collections import deque

def power_sum(selected):
    p_sum = 0
    partner = list(combinations(selected, 2))
    for p in partner:
        p_sum += power[p[0]-1][p[1]-1] + power[p[1]-1][p[0]-1]

    return p_sum


input = sys.stdin.readline
N = int(input())
power = []
answer = float('inf')

for _ in range(N):
    power.append([int(x) for x in input().split()])

team = [x for x in range(1, N+1)]
c = deque(list(combinations(team, N//2)))

while c:
    start = c.popleft()
    link = c.pop()
    answer = min(abs(power_sum(start)-power_sum(link)), answer)

print(answer)
