# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0

    # win - 이긴 사람 : 진 사람 / lose - 진 사람 : 이긴 사람
    win = {x: set() for x in range(1, n + 1)}
    lose = {x: set() for x in range(1, n + 1)}

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    # i를 이긴 사람들은 i가 이긴 사람들 또한 이긴다.
    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])
            # win과 lose의 합이 n-1일 경우, 해당 사람의 순위를 알 수 있다.

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer