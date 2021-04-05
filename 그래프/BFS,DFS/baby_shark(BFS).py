# https://www.acmicpc.net/problem/16236

# 처음 아기 상어 크기는 2
# 자기보다 큰 물고기는 지나갈 수 없음
# 자기보다 작은 물고기만 먹을 수 있음
# 먹을 수 있는 물고기가 1마리 이상이면, 거리가 가장 가까운 물고기를 먹으러 감
# ** 거리가 가까운 물고기가 여러 마리면 가장 위 -> 왼쪽에 있는 물고기를 먹음 **
# 자기 크기만큼의 물고기를 먹을 때마다 크기가 1 증가

import sys
from collections import deque
import heapq
# 최단거리 찾기에서 과정 중에 따로 조건이 없으면 치킨집처럼 그냥 abs(x1-x2) + abs(y1-y2)로 가능
# 근데 얘는 조건이 있어서 불가능

directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
G = []
N = int(input())
size = 2
fish = {i: 0 for i in range(1, 7)}
pos = []

def bfs(x, y):
    global G, N, size, fish, pos
    queue = deque()
    queue.append([x, y, 0])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    eat = [] # 소요시간, x, y

    while queue:
        a, b, time = queue.popleft()
        if G[a][b] != 0 and G[a][b] < size:
            heapq.heappush(eat, (time, a, b))
        for d in directions:
            new_a = a + d[0]
            new_b = b + d[1]
            if 0 <= new_a < N and 0 <= new_b < N:
                if not visited[new_a][new_b]:
                    if G[new_a][new_b] <= size:
                        queue.append([new_a, new_b, time+1])
                        visited[new_a][new_b] = True
    if eat:
        fish[G[eat[0][1]][eat[0][2]]] -= 1
        G[eat[0][1]][eat[0][2]] = 0
        pos = [eat[0][1], eat[0][2]]
        return True, eat[0][0]
    return False, time

def solution():
    global G, N, size, fish, pos
    input = sys.stdin.readline
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            if tmp[j] == 9:
                pos = [i, j]
            elif tmp[j] != 0:
                fish[tmp[j]] += 1
        G.append(tmp)
    answer = 0
    eaten_fish = 0
    G[pos[0]][pos[1]] = 0

    while sum(fish.values()) != 0:
        isEatable, duration = bfs(pos[0], pos[1])
        if isEatable:
            answer += duration
            eaten_fish += 1
            if eaten_fish == size:
                eaten_fish = 0
                size += 1
        else:
            break
    print(answer)

solution()