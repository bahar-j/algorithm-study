# https://www.acmicpc.net/problem/1707
# 모든 간선이 연결돼있는 경우만 이분 그래프가 되는 건 아님!

import sys
from collections import deque


def answer():
    check = [0] * (V + 1)
    queue = deque([])

    for i in range(1, V+1):
        if check[i] == 0:
            queue.append([i, 1])
            check[i] = 1
        while queue:
            now, part = queue.popleft()
            for adjacent in G[now]:
                if check[adjacent] == 0:
                    check[adjacent] = part*-1
                    queue.append([adjacent, part*-1])
                else:
                    if part == check[adjacent]:
                        print('NO')
                        return
    print('YES')

input = sys.stdin.readline
N_TEST = int(input())

for _ in range(N_TEST):
    V, E = map(int, input().split())
    G = {i: [] for i in range(1, V+1)}
    for _ in range(E):
        start_, end_ = map(int, input().split())
        G[start_].append(end_)
        G[end_].append(start_)
    answer()

