# https://www.acmicpc.net/problem/14499
# 구현은 문제 잘 읽고 구현할 항목 적어두기 !

# 동쪽(1) 1->3, 2->2, 3->6, 4->1, 5->5, 6->4
# 서쪽(2) 1->4, 2->2, 3->1, 4->6, 5->5, 6->3
# 북쪽(3) 1->2, 2->6, 3->3, 4->4, 5->1, 6->5
# 남쪽(4) 1->5, 2->1, 3->3, 4->4, 5->6, 6->2

import sys

move_by_dir = [[0,0,0,0,0,0,0], [0,3,2,6,1,5,4], [0,4,2,1,6,5,3],
                [0,2,6,3,4,1,5], [0,5,1,3,4,6,2]]

def move(val, idx, dice, visited, order):
    visited[idx] = True
    copy_to = move_by_dir[order][idx]
    tmp = dice[copy_to]
    dice[copy_to] = val

    if visited.count(True) == 6:
        return

    if idx != copy_to:
        if not visited[copy_to]:
            move(tmp, copy_to, dice, visited, order)


def solution():
    input = sys.stdin.readline
    N, M, x, y, K = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))
    dice = [0] * 7
    dice[6] = G[x][y]
    directions = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))

    for order in orders:
        new_x = x + directions[order][0]
        new_y = y + directions[order][1]
        if 0 <= new_x < N and 0 <= new_y < M:
            visited = [False] * 7
            while visited.count(True) != 6:
                for i in range(1, 7):
                    if not visited[i]:
                        move(dice[i], i, dice, visited, order)
            if G[new_x][new_y] != 0:
                dice[6] = G[new_x][new_y]
                G[new_x][new_y] = 0
            else:
                G[new_x][new_y] = dice[6]
            x = new_x
            y = new_y
            print(dice[1])

solution()
