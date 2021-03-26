# https://www.acmicpc.net/problem/11048
# directions 안하고 그냥 두 가지 경우 중에 max로 넣어주면
# DP 리스트도 따로 필요 없음 (원래 그래프의 값 유지하려고 따로 만들어준거라서..)

import sys
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
G = []
directions = ((1, 0), (0, 1))

for _ in range(N):
    G.append(list(map(int, input().split())))

DP = copy.deepcopy(G)

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        for d in directions:
            if 0 <= i-d[0] < N and 0 <= j-d[1] < M:
                DP[i][j] = max(DP[i-d[0]][j-d[1]] + G[i][j], DP[i][j])

print(DP[-1][-1])
