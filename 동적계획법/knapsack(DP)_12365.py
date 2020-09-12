import sys

N, K = map(int, sys.stdin.readline().split())

KNAPSACK = [0]*(K+1)

for i in range(N):
    # 하나씩 가방에 넣음
    W, V = map(int, sys.stdin.readline().split())
    # 현재 상황에서 무게 0 ~ K인 경우의 최대 가치 업데이트
    for j in range(K, W-1, -1):
        KNAPSACK[j] = max(KNAPSACK[j], KNAPSACK[j-W]+V)

print(max(KNAPSACK))
