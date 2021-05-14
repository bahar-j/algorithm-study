# https://www.acmicpc.net/problem/20040

import sys

def find_parent(a, parents):
    if parents[a] == a:
        return a
    return find_parent(parents[a], parents)

def union(a, b, parents):
    acient_a, acient_b = find_parent(a, parents), find_parent(b, parents)

    if acient_a == acient_b:
        return True

    if acient_a < acient_b:
        parents[acient_b] = acient_a
    else:
        parents[acient_a] = acient_b

    return False

def solution(n, spots):
    parents = [i for i in range(n)]
    idx = -1

    for i in range(len(spots)):
        spot = spots[i]
        if union(spot[0], spot[1], parents):
            idx = i+1
            break

    print(idx) if idx != -1 else print(0)


input = sys.stdin.readline
N, M = map(int, input().split())
spots = [list(map(int, input().split())) for _ in range(M)]

solution(N, spots)