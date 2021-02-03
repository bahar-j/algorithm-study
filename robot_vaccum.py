import sys

sys.setrecursionlimit(10**6)

def clean(r, c, d, n_turn):
    global cleaned

    if map[r][c] == 0:
        map[r][c] = 2
        cleaned += 1

    if n_turn == 4:
        back = turn_back[d]
        new_r = r + back[0]
        new_c = c + back[1]
        if 0 <= new_r < N and 0 <= new_c < M:
            if map[new_r][new_c] != 1:
                clean(new_r, new_c, d, 0)
                return
            else:
                return

    left_r, left_c, new_d = turn_left[d]
    new_r = r + left_r
    new_c = c + left_c
    if 0 <= new_r < N and 0 <= new_c < M:
        if map[new_r][new_c] == 0:
            clean(new_r, new_c, new_d, 0)
        else:
            clean(r, c, new_d, n_turn + 1)
    else:
        back = turn_back[d]
        new_r = r + back[0]
        new_c = c + back[1]
        if 0 <= new_r < N and 0 <= new_c < M:
            if map[new_r][new_c] != 1:
                clean(new_r, new_c, d, 0)
                return
            else:
                return


input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
turn_left = {0: [0, -1, 3], 1: [-1, 0, 0], 2: [0, 1, 1], 3: [1, 0, 2]}
turn_back = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
map = []
cleaned = 0

for _ in range(N):
    map.append([int(x) for x in input().split()])

clean(r, c, d, 0)
print(cleaned)
