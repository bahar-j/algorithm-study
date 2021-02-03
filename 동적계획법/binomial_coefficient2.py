# https://www.acmicpc.net/problem/11051

# n개의 원소 중 r개의 원소를 뽑아내는 경우의 수는
# 맨 마지막 원소 n을 제외한
# n-1개의 원소 중 r-1개를 뽑아내는 경우의 수
# +
# n-1개의 원소 중 r개를 뽑아내는 경우의 수

N, K = map(int, input().split())

DP = [[] for _ in range(N+1)]
DP[0] = 1
DP[1].extend([1, 1])

for i in range(2, N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            DP[i].append(1)
        else:
            DP[i].append(DP[i-1][j-1] + DP[i-1][j])

print(DP[N][K] % 10_007)

