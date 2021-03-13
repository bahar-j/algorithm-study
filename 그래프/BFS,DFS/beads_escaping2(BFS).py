# https://www.acmicpc.net/problem/13460
# 틀린 이유:
# visited 체크를 빨간 파란 공 둘 다 고려해서 4차원으로 해줬어야함
# 구슬 이동 순서 고려해서 디테일하게 구현
# 최단거리 -> BFS

import sys
from collections import deque

def move(pos, d):
    x, y = pos
    is_done = False
    move = 0
    while True:
        if G[x+d[0]][y+d[1]] == 'O':
            is_done = True
            return [x+d[0], y+d[1]], is_done, move+1
        elif G[x+d[0]][y+d[1]] != '#':
            x += d[0]
            y += d[1]
            move += 1
        else:
            return [x, y], is_done, move

input = sys.stdin.readline
N, M = map(int, input().split())
G = []
r_pos = []
b_pos = []
cnt = 0
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
answer = float('inf')

for i in range(N):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == 'R':
            r_pos = [i, j]
        elif tmp[j] == 'B':
            b_pos = [i, j]
    G.append(tmp)

queue = deque([])
queue.append([r_pos, b_pos, cnt])
visited[r_pos[0]][r_pos[1]][b_pos[0]][b_pos[1]] = True

while queue:
    r_now, b_now, cnt_now = queue.popleft()

    if cnt_now > 10:
        break

    for d in directions:
        new_r, r_is_done, r_move = move(r_now, d)
        new_b, b_is_done, b_move = move(b_now, d)

        if b_is_done:
            continue
        if r_is_done:
            answer = min(answer, cnt_now + 1)

        if new_r == new_b:
            if r_move > b_move:
                new_r = [new_r[0]-d[0], new_r[1] - d[1]]
            else:
                new_b = [new_b[0]-d[0], new_b[1] - d[1]]

        if not visited[new_r[0]][new_r[1]][new_b[0]][new_b[1]]:
            queue.append([new_r, new_b, cnt_now+1])
            visited[new_r[0]][new_r[1]][new_b[0]][new_b[1]] = True

if answer == float('inf') or answer > 10:
    print(-1)
else:
    print(answer)
