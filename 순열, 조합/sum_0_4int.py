#https://www.acmicpc.net/problem/7453

import sys

input = sys.stdin.readline
N = int(input())
answer = 0

A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum_ab = {}
for i in range(N):
    for j in range(N):
        a, b = A[i], B[j]
        try:
            sum_ab[a+b] += 1
        except:
            sum_ab[a+b] = 1

for i in range(N):
    for j in range(N):
        c, d = C[i], D[j]
        try:
            answer += sum_ab[-(c+d)]
        except:
            continue

print(answer)