# https://www.acmicpc.net/problem/19941

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
G = list(input().rstrip())
answer = 0

for i in range(len(G)):
    if G[i] == 'H':
        for offset in range(-K, K+1):
            point = i + offset
            if 0 <= point < len(G) and G[point] == 'P':
                G[point] = 'X'
                answer += 1
                break
            elif 0 <= point < len(G) and G[point] == 'P':
                G[point] = 'X'
                answer += 1
                break
        G[i] = 'X'

print(answer)
