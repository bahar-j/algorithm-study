# https://www.acmicpc.net/problem/4963
# DFS는 재귀 호출 스택 터짐

import sys

sys.setrecursionlimit(10**6)

def dfs(h, w):
    G[h][w] = '2'
    permutations = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (-1, -1), (1, 1)]

    for item in permutations:
        if G[h + item[0]][w + item[1]] == '1':
            dfs(h + item[0], w + item[1])

while True:
    G = []
    result = 0
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    G.append(['0'] * (W + 2))
    for _ in range(H):
        temp = ['0']
        temp.extend(list(sys.stdin.readline().split()))
        temp.append('0')
        G.append(temp)
    G.append(['0'] * (W + 2))
    for h in range(1, H+1):
        for w in range(1, W+1):
            if G[h][w] == '1':
                dfs(h, w)
                result += 1
    print(result)
