# https://programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    # 모든 지점까지 함께 가는 최단 경로 // 2 (s ~ stopover)
    # 해당 지점을 출발점으로 놓고 거기서 각자의 집으로 가는 최단 경로 (stopover ~ a / b)
    INF = float('inf')
    answer = INF
    DP = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        DP[i][i] = 0

    for fare in fares:
        start, end, value = fare
        DP[start][end] = value
        DP[end][start] = value

    for stopover in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                DP[i][j] = min(DP[i][stopover] + DP[stopover][j], DP[i][j])

    for stopover in range(1, n + 1):
        if DP[s][stopover] != INF and DP[stopover][a] != INF and DP[stopover][b] != INF:
            tmp_fare = DP[s][stopover] + DP[stopover][a] + DP[stopover][b]
            answer = min(tmp_fare, answer)

    return answer