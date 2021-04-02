# https://www.acmicpc.net/problem/3190

# 사과를 먹으면 길이가 늘어남
# 벽 또는 자기 몸과 부딪히면 끝
# 처음에는 오른쪽을 향함
# 다음 칸으로 향한다/사과가 있으면 늘어난 채로/사과가 없으면 꼬리가 줄어듦

# 방향 변경 X, C에서 X초가 끝난 뒤이니까
# 실제 이동을 하는거는 X+1초에서

import sys
from collections import defaultdict, deque

def change(d, c):
    # 상(0), 우(1), 하(2), 좌(3)
    if c == 'L':
        new_d = (d - 1) % 4 # 4로 나누면 나머지는 0~3 사이로 나옴
    elif c == 'D':
        new_d = (d + 1) % 4
    return new_d

def move(d):
    if d == 0:
        return (-1, 0)
    elif d == 1:
        return (0, 1)
    elif d == 2:
        return (1, 0)
    elif d == 3:
        return (0, -1)

def start():
    global answer
    direction = 1
    time = 1
    visited = deque()
    x, y = 0, 0
    visited.append([x, y])

    while True:
        d_x, d_y = move(direction)
        x, y = x + d_x, y + d_y

        # 이동 x, 시간 리턴
        if x < 0 or x >= N or y < 0 or y >= N or G[x][y] == 2:
            return time

        # 이동
        visited.append([x, y])

        if G[x][y] != 1:
            tail_x, tail_y = visited.popleft()
            G[tail_x][tail_y] = 0
        G[x][y] = 2

        # 이후 방향 변경
        if times[time]:
            direction = change(direction, times[time])

        # 시간 증가
        time += 1

input = sys.stdin.readline
N = int(input())
K = int(input())
G = [[0]*N for _ in range(N)]
G[0][0] = 2
answer = 0

for _ in range(K):
    x, y = map(int, input().split())
    G[x-1][y-1] = 1

L = int(input())
times = defaultdict(str)
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C

print(start())