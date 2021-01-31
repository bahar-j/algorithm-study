# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
boxes = []
queue = deque([])
cnt = 0
day = 0

for h in range(H):
    tmp = []
    for n in range(N):
        tmp2 = list(map(int, input().split()))
        for m in range(M):
            if tmp2[m] == 1:
                queue.append((h, n, m))
            if tmp2[m] != 0:
                cnt += 1
        tmp.append(tmp2)
    boxes.append(tmp)

while queue:
    h, n, m = queue.popleft()
    day = boxes[h][n][m]
    directions = ((0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0))

    for d in directions:
        new_h = h + d[0]
        new_n = n + d[1]
        new_m = m + d[2]
        if 0 <= new_h < H and 0 <= new_n < N and 0 <= new_m <M:
            if boxes[new_h][new_n][new_m] == 0:
                queue.append((new_h, new_n, new_m))
                cnt += 1
                boxes[new_h][new_n][new_m] = day+1


if cnt != N*M*H:
    print(-1)
else:
    print(day-1)