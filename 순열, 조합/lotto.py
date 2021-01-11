# https://www.acmicpc.net/problem/6603
from sys import stdin
import itertools

while True:
    tmp = stdin.readline().split(maxsplit=1)
    if tmp[0] == '0':
        break
    K, S = int(tmp[0]), tmp[1]
    S = list(S.split())
    combi = list(itertools.combinations(S, 6))
    for item in combi:
        print(' '.join(item))
    print()
