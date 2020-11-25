# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0

    # 맵 만들기
    map = [[1] * m for _ in range(n)]
    map[0][0] = 0

    # 웅덩이 - 열, 행
    for i in range(len(puddles)):
        y, x = puddles[i]
        map[x - 1][y - 1] = 0

    # 최단경로
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                continue
            elif i == 0:
                # 그 전 값이 출발점이 아닌 경우
                if j - 1 != 0:
                    map[i][j] = map[i][j - 1]
            elif j == 0:
                if i - 1 != 0:
                    map[i][j] = map[i - 1][j]
            else:
                map[i][j] = map[i - 1][j] + map[i][j - 1]

    answer = map[-1][-1]
    answer %= 1000000007

    return answer