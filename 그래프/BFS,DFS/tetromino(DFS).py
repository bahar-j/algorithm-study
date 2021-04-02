# https://www.acmicpc.net/problem/14500
# BFS로 visited 관리하기 힘들때는 DFS가 나음

import sys

def dfs(x, y, cnt, tmp_sum):
    global answer
    if cnt == 4:
        answer = max(answer, tmp_sum)
        return
    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if 0 <= new_x < N and 0 <= new_y < M:
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                dfs(new_x, new_y, cnt+1, tmp_sum+G[new_x][new_y])
                visited[new_x][new_y] = False

def middle_finger(x, y):
    global answer

    for m in m_finger:
        try:
            num = G[x][y] + G[x+m[0][0]][y+m[0][1]] + G[x+m[1][0]][y+m[1][1]] + G[x+m[2][0]][y+m[2][1]]
        except:
            num = 0
        answer = max(answer, num)

input = sys.stdin.readline
N, M = map(int, input().split())
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
m_finger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]],
[[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]
G = [list(map(int, input().split())) for _ in range(N)]
answer = 0
visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, G[i][j])
        visited[i][j] = False
        middle_finger(i, j)

print(answer)