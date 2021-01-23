# https://www.acmicpc.net/problem/1780
import sys

def is_same(start_x, start_y, width):
    num = G[start_x][start_y]
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + width):
            if G[i][j] != num:
                return False
    return True

def cut_paper(start_x, start_y, width):
    for i in range(3):
        for j in range(3):
            new_x = start_x + width//3 * i
            new_y = start_y + width//3 * j
            if is_same(new_x, new_y, width//3):
                count[G[new_x][new_y]] += 1
            else:
                cut_paper(new_x, new_y, width//3)

input = sys.stdin.readline
N = int(input())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))
count = {i: 0 for i in range(-1, 2)}

if is_same(0, 0, N):
    count[G[0][0]] = 1
else:
    cut_paper(0, 0, N)

for key in count:
    print(count[key])