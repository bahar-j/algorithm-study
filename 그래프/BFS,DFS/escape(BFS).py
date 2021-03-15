# https://www.acmicpc.net/problem/3055
# 물 이동을 한 턴마다 해줘야하는데 매 이동마다 해준게 문제

import sys
from collections import deque

def bfs():
    queue = deque([])
    queue.append([my_pos, 1])
    visited = [[False] * C for _ in range(R)]
    visited[my_pos[0]][my_pos[1]] = True

    while queue:
        qlen = len(queue)
        while qlen:
            my_now, time = queue.popleft()

            for d in directions:
                new_x = my_now[0] + d[0]
                new_y = my_now[1] + d[1]
                if 0 <= new_x < R and 0 <= new_y < C:
                    if G[new_x][new_y] == 'D':
                        print(time)
                        return
                    elif G[new_x][new_y] == '.' and not visited[new_x][new_y]:
                        queue.append([[new_x, new_y], time + 1])
                        visited[new_x][new_y] = True
            qlen -= 1
        move_water()
    print('KAKTUS')
    return
def move_water():
    wlen = len(water_pos)
    for i in range(wlen):
        x, y = water_pos[i]
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x < R and 0 <= new_y < C:
                if G[new_x][new_y] == '.':
                    G[new_x][new_y] = '*'
                    water_pos.append([new_x, new_y])


input = sys.stdin.readline

R, C = map(int, input().split())
G = []
my_pos = []
water_pos = []
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i in range(R):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == 'S':
            my_pos = [i, j]
        elif tmp[j] == '*':
            water_pos.append([i, j])
    G.append(tmp)

move_water()
G[my_pos[0]][my_pos[1]] = '.'
bfs()

