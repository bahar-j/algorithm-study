# https://www.acmicpc.net/problem/2667

size = int(input())

town = []

visited = []

prev_visited = 0

num_town = 0

num_building = []

for i in range (size):
    town.append(list(input()))

print(town)

def DFS(x, y):
    visited.append((x,y))
    # 오른쪽
    if ( y <= size-2 ):
        if ( town[x][y+1] == '1' ):
            if ((x, y+1) not in visited):
                DFS(x, y+1)
    # 왼쪽
    if ( y >= 1 ): 
        if ( town[x][y-1] == '1' ):
            if ((x, y-1) not in visited):
                DFS(x, y-1)
    # 위
    if ( x >= 1 ):
        if ( town[x-1][y] == '1' ):
            if ((x-1, y) not in visited):
                DFS(x-1, y)
    # 아래
    if ( x <= size-2 ):
        if ( town[x+1][y] == '1' ):
            if ((x+1, y) not in visited):
                DFS(x+1, y)

for i in range (size):
    for j in range (size):
        if ((town[i][j] == '1') and ((i, j) not in visited)):
            DFS(i, j)
            num_town += 1
            if (prev_visited == 0):
                prev_visited = len(visited)
                num_building.append(prev_visited)
            else :
                num_building.append(len(visited)-prev_visited)

print(num_town)
for i in range (num_town):
    print(num_building[i])