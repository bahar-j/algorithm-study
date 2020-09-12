import sys

N = int(sys.stdin.readline().strip())
score_per_wine = [int(sys.stdin.readline().strip()) for i in range(N)]

for _ in range(3):
    score_per_wine.insert(0, 0)

WINE = [0] * (N+3)

for i in range(3, N+3):
    tmp = max(WINE[i-3]+score_per_wine[i-1], WINE[i-2]) + score_per_wine[i]
    WINE[i] = max(tmp, WINE[i-1])

print(WINE[-1])
