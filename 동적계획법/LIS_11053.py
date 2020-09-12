import sys

N = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))
sequence.insert(0, 0)

LIS = [0] * (N+1)
tmp = list()

for i in range(1, N+1):
    now_search = sequence[i]
    for j in range(i-1, -1, -1):
        if sequence[j] < now_search:
            tmp.append(LIS[j])
    LIS[i] = max(tmp) + 1
    tmp.clear()

print(max(LIS))
