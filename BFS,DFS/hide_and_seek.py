import sys
from collections import deque
from collections import defaultdict

me, sis = map(int, sys.stdin.readline().split())

queue = deque([])
queue.append((me, 0))
visited = defaultdict(int)
visited[me] = 1

while queue:

    pos, time = queue.popleft()

    if pos == sis:
        print(time)
        break

    if (pos-1 == sis) or (pos+1 == sis) or (pos*2 == sis):
        print(time+1)
        break

    if(0 <= pos-1) and (pos-1 <= 100000) and (visited[pos-1] != 1):
        queue.append((pos-1, time+1))
        visited[pos-1] = 1

    if (0 <= pos + 1) and (pos + 1 <= 100000) and (visited[pos+1] != 1):
        queue.append((pos + 1, time + 1))
        visited[pos+1] = 1

    if (0 <= pos * 2) and (pos * 2 <= 100000) and (visited[pos*2] != 1):
        queue.append((pos * 2, time + 1))
        visited[pos*2] = 1

