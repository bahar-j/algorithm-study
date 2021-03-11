# https://www.acmicpc.net/problem/11660

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
G = []
answer = []
DP = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    G.append(tmp)
    sum = 0
    tmp2 = []
    for t in tmp:
        sum += t
        tmp2.append(sum)
    DP.append(tmp2)


for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    sum = 0
    for y in range(y1, y2+1):
        if x1 > 1:
            sum += DP[y-1][x2-1] - DP[y-1][x1-2]
        else:
            sum += DP[y-1][x2-1]
    answer.append(sum)

for a in answer:
    print(a)