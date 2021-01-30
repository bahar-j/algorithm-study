# https://www.acmicpc.net/problem/11404

from sys import stdin

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
INF = float('inf')

G = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신으로 가는 경우
for i in range(1, N+1):
    G[i][i] = 0

# 모든 노드에서 인접 노드로 가는 비용 setting
for _ in range(M):
    a, b, cost = map(int, stdin.readline().split())
    if G[a][b] > cost:
        G[a][b] = cost

# (모든 경유지 k에 대해서) i->j로 경유지 k를 거쳐서 가는 방법
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

# 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if G[i][j] == INF:
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()
