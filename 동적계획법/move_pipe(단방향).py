# https://www.acmicpc.net/problem/17070
import sys
# DP[행][열][방향]
# 문제 잘 읽자........

def check(x, y):
    if 0 <= x < N and 0 <= y < N and house[x][y] != 1:
        return True
    return False

input = sys.stdin.readline
N = int(input())
house = []

for _ in range(N):
    house.append([int(x) for x in input().split()])

DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

DP[0][0][0] = 1
DP[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        if house[i][j] == 1:
            continue
        for d in range(3):
            if DP[i][j][d] == 0:
                continue
            if d == 0: # 현재 가로 -> 다음 가로 or 대각
                if check(i, j+1):
                    DP[i][j+1][0] += DP[i][j][d]
                    if check(i+1, j+1) and check(i+1, j):
                        DP[i+1][j+1][2] += DP[i][j][d]
            elif d == 1: # 현재 세로 -> 다음 세로 or 대각
                if check(i+1, j):
                    DP[i+1][j][1] += DP[i][j][d]
                    if check(i+1, j+1) and check(i, j+1):
                        DP[i+1][j+1][2] += DP[i][j][d]
            else:
                if check(i, j+1):
                    DP[i][j+1][0] += DP[i][j][d]
                if check(i+1, j):
                    DP[i+1][j][1] += DP[i][j][d]
                    if check(i+1, j+1) and check(i, j+1):
                        DP[i+1][j+1][2] += DP[i][j][d]

print(sum(DP[-1][-1]))
