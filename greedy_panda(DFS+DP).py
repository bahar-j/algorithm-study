# https://www.acmicpc.net/problem/1937
# 가장 대나무가 적은 곳에서 시작 ? (X)
# 그 전 지역보다 대나무가 많은 곳으로 이동 !!
# 가능한 모든 경로 탐색 ? (0)
# 메모리제이션

import sys

sys.setrecursionlimit(10**6)

def dfs(i, j):
    global DAYS
    if DAYS[i][j]:
        return DAYS[i][j]
    DAYS[i][j] = 1
    for d in directions:
        new_i = i + d[0]
        new_j = j + d[1]
        if 0 <= new_i < N and 0 <= new_j < N:
            if G[i][j] < G[new_i][new_j]:
                # 이미 방문했던 곳 찾을 때까지 dfs하다가 찾으면 하나씩 거슬러오면서 1씩 더해줌
                DAYS[i][j] = max(1, dfs(new_i, new_j)+1)
    return DAYS[i][j]

input = sys.stdin.readline
N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
DAYS = [[0]*N for _ in range(N)]

def solution():
    answer = 0
    for i in range(N):
        for j in range(N):
            # 여기서 받은 값은 끝지점 찍고 처음까지 거꾸로 돌아왔을 때 그 지점의 값
            # 즉 DP[i][j]는 그 지점에서 출발했을 때 최대 값
            answer = max(answer, dfs(i, j))

    return answer

print(solution())