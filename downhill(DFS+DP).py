# https://www.acmicpc.net/problem/1520
# 한방향 길찾기는 DP인데
# 얘는 그때그때 네 방향 다 봐야해서 DFS + DP

# <solution>
# 원래 한방향으로 갈때는 지금꺼의 DP를 이후꺼의 DP에다가 더해주면 되는데
# 4방향이라 그렇게 하면 더해준 이후에 값이 갱신돼서 번복해줘야하는 상황이 생김

# 그래서 지금꺼의 DP에다가 4방향의 DP를 더해주는데,
# 그 값 자체도 dfs로 4방향 확인
# 대신 이미 방문한 곳이면 바로 그 자리의 DP 리턴해서 더해줌
# 이 과정을 통해
# * a *
# b c d
# * e *
# 순서로 있을 때 c에서 아직 DP 값이 확정되지 않은 d와 e의 값을 더해주는 것을 보류할 수 있음

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M, N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
DP = [[-1]*N for _ in range(M)]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if DP[x][y] != -1:
        return DP[x][y]
    DP[x][y] = 0
    for d in directions:
        new_x = x - d[0]
        new_y = y - d[1]
        if 0 <= new_x < M and 0 <= new_y < N:
            if G[new_x][new_y] < G[x][y]:
                DP[x][y] += dfs(new_x, new_y)
    return DP[x][y]

print(dfs(0, 0))
