# https://www.acmicpc.net/problem/2589
# 최단거리로 이동하는데 가장 오래걸리는 육지
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
G = [list(input().rstrip()) for _ in range(N)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(x, y):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append([x, y, 0])
    visited[x][y] = True
    tmp_answer = 0

    while queue:
        a, b, length = queue.popleft()
        if tmp_answer < length:
            tmp_answer = length
        for d in directions:
            new_a = a + d[0]
            new_b = b + d[1]
            if 0 <= new_a < N and 0 <= new_b < M:
                if not visited[new_a][new_b] and G[new_a][new_b] == "L":
                    queue.append([new_a, new_b, length+1])
                    visited[new_a][new_b] = True
    return tmp_answer


def solution():
    answer = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == "L":
                answer = max(bfs(i, j), answer)
    return answer

print(solution())