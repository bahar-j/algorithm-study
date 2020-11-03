# https://www.acmicpc.net/problem/15649

import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(now, path):

    path += str(now) + " "

    if len(path) == m*2:
        print(path.rstrip())
        return

    for i in range(1, n+1):
        if str(i) not in path:
            dfs(i, path)


for j in range(1, n+1):
    dfs(j, '')




