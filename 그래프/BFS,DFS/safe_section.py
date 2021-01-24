# https://www.acmicpc.net/problem/2468
import sys

sys.setrecursionlimit(10**9)

def dfs(x, y, rain, visited):
    visited[x][y] = True
    for direction in directions:
        new_x = direction[0] + x
        new_y = direction[1] + y
        if 0 <= new_x < N and 0 <= new_y < N:
            if G[new_x][new_y] > rain and not visited[new_x][new_y]:
                dfs(new_x, new_y, rain, visited)

input = sys.stdin.readline
N = int(input())
G = []
max_num = 0
min_num = 101
max_safe = 1 # 아무 지역도 물에 잠기지 않으면 1
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

for _ in range(N):
    str_list = list(input().split())
    tmp = []
    for i in range(N):
        num = int(str_list[i])
        if num <= min_num:
            min_num = num
        if num >= max_num:
            max_num = num
        tmp.append(num)
    G.append(tmp)

for rain in range(min_num, max_num):
    safe_section = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for m in range(N):
        for n in range(N):
            if G[m][n] > rain and not visited[m][n]:
                    dfs(m, n, rain, visited)
                    safe_section += 1
    max_safe = max(safe_section, max_safe)

print(max_safe)
