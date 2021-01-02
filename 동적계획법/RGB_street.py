# https://www.acmicpc.net/problem/1149
from sys import stdin

LINE = int(input())
G = []
RGB_MIN = [[0, 0, 0] for _ in range(LINE)]

for _ in range(LINE):
    G.append(list(map(int, stdin.readline().split())))

for i in range(LINE):
    if i == 0:
        RGB_MIN[i][0] = G[i][0]
        RGB_MIN[i][1] = G[i][1]
        RGB_MIN[i][2] = G[i][2]
    else:
        RGB_MIN[i][0] = min(RGB_MIN[i-1][1], RGB_MIN[i-1][2]) + G[i][0]
        RGB_MIN[i][1] = min(RGB_MIN[i-1][0], RGB_MIN[i-1][2]) + G[i][1]
        RGB_MIN[i][2] = min(RGB_MIN[i-1][0], RGB_MIN[i-1][1]) + G[i][2]

print(min(RGB_MIN[-1]))
