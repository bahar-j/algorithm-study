# https://www.acmicpc.net/problem/11279

from sys import stdin
import heapq

N = int(stdin.readline())
maxheap = []

for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        if not maxheap:
            print(0)
        else:
            print(heapq.heappop(maxheap)[1])
    else:
        heapq.heappush(maxheap, (-num, num))
