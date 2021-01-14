# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0

    def DFS(x, y):
        computers[x][y] = 2
        computers[y][x] = 2

        for i in range(0, n):
            if computers[y][i] == 1:
                DFS(y, i)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                DFS(i, j)
                answer += 1

    return answer