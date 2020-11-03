# https://www.acmicpc.net/problem/2178

import sys

row, column = map(int, sys.stdin.readline().split())
maze = []
visited = []
queue = []

for i in range (row):
    maze.append(list(sys.stdin.readline()))

D = [[0] * (column) for _ in range(row)]

queue.append((0, 0))
visited.append((0, 0))

while( len(queue) != 0 ):
    x, y = queue[0]

    if ( y+1 < column ):
        if ( (maze[x][y+1] == '1') and ((x, y+1) not in visited) ):
            D[x][y+1] = D[x][y] + 1
            queue.append((x, y+1))
            visited.append((x, y+1))
            if((x == row-1) and (y+1 == column-1) ):
                break

    if ( x+1 < row ):
        if ( maze[x+1][y] == '1' and ((x+1, y) not in visited) ):
            D[x+1][y] = D[x][y] + 1
            queue.append((x+1, y))
            visited.append((x+1, y))
            if((x+1 == row-1) and (y == column-1)):
                break

    # 위
    if ( x-1 >= 0 ):
        if ( maze[x-1][y] == '1' and ((x-1, y) not in visited) ):
            D[x-1][y] = D[x][y] + 1
            queue.append((x-1, y))
            visited.append((x-1, y))
            if((x-1 == row-1) and (y == column-1)):
                break
    
    # 왼쪽
    if ( y-1 >= 0 ):
        if ( maze[x][y-1] == '1' and ((x, y-1) not in visited) ):
            D[x][y-1] = D[x][y] + 1
            queue.append((x, y-1))
            visited.append((x, y-1))
            if((x == row-1) and (y-1 == column-1) ):
                break
    
    del queue[0]

print(D[-1][-1]+1)
