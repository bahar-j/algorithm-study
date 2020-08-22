import sys
from collections import deque

column, row = map(int, sys.stdin.readline().split())
box = []
queue = deque([])
day = 0
cnt = 0

box.append([1] * (column + 2))
for i in range(1, row + 1):
    box.append([1])
    idx = 0
    for j in map(int, sys.stdin.readline().split()):
        idx += 1
        box[i].append(j)
        if (j == 1) and (i != 0) and (i != row+1) and (idx != 0) and (idx != column+1):
            queue.append((i, idx))
        if j == -1:
            cnt += 1
    box[i].append(1)
box.append([1] * (column + 2))

while queue:
    x, y = queue.popleft()
    day = box[x][y] + 1

    if box[x][y+1] == 0:
        queue.append((x, y+1))
        box[x][y+1] = day

    if box[x+1][y] == 0:
        queue.append((x+1, y))
        box[x+1][y] = day

    if box[x][y-1] == 0:
        queue.append((x, y-1))
        box[x][y-1] = day

    if box[x-1][y] == 0:
        queue.append((x-1, y))
        box[x-1][y] = day

    cnt += 1

if cnt != column*row:
    print(-1)
else:  
    print(day-2)
