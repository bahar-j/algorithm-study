# https://www.acmicpc.net/problem/9465
from sys import stdin

TEST_CASE = int(input())
answer = []

for _ in range(TEST_CASE):
    width = int(input())
    STICKER = [[0] * width for _ in range(2)]
    scores = []
    for j in range(2):
        scores.append(list(map(int, stdin.readline().split())))
    for i in range(width):
        if i == 0:
            STICKER[0][0] = scores[0][0]
            STICKER[1][0] = scores[1][0]
        else:
            STICKER[0][i] = max(STICKER[1][i-1] + scores[0][i], STICKER[1][i-2] + scores[0][i])
            STICKER[1][i] = max(STICKER[0][i-1] + scores[1][i], STICKER[0][i-2] + scores[1][i])
    answer.append(max(STICKER[0][-1], STICKER[1][-1]))

for i in range(TEST_CASE):
    print(answer[i])

