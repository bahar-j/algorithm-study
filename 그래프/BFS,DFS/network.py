# https://programmers.co.kr/learn/courses/30/lessons/43162

def DFS(x, y, n, computers):
    computers[x][y] = 2
    computers[y][x] = 2

    for i in range(0, n):
        if computers[y][i] == 1:
            DFS(y, i, n, computers)


def solution(n, computers):
    answer = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                DFS(i, j, n, computers)
                answer += 1

    return answer