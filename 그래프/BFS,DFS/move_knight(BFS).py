# https://www.acmicpc.net/problem/7562
# BFS로만 가능

from sys import stdin
from collections import deque

N_TEST_CASE = int(input())
directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

for _ in range(N_TEST_CASE):
    width = int(input())
    chess = [[0]*width for _ in range(width)]
    start_x, start_y = map(int, stdin.readline().split())
    chess[start_x][start_y] = 1
    dest_x, dest_y = map(int, stdin.readline().split())

    will_visit = deque([])
    will_visit.append([start_x, start_y, 0])

    min_n_move = float('inf')
    n_move = 0

    while will_visit:
        now_x, now_y, n_move = will_visit.popleft()

        if now_x == dest_x and now_y == dest_y:
            min_n_move = min(n_move, min_n_move)
            break

        for direction in directions:
            if 0 <= now_x+direction[0] < width and 0 <= now_y+direction[1] < width:
                if chess[now_x+direction[0]][now_y+direction[1]] == 0:
                    will_visit.append([now_x+direction[0], now_y+direction[1], n_move+1])
                    chess[now_x+direction[0]][now_y+direction[1]] = 1

    print(min_n_move)








