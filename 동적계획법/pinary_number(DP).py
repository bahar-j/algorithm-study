# https://www.acmicpc.net/problem/2193

# DP[i] = DP[i-1][0] + DP[i-1][1], DP[i-1][0]
# DP[1] = 0, 1
# DP[2] = 1, 0
# DP[3] = 1 + 0, 1

N = int(input())

DP = [[0, 0], [0, 1]]

for i in range(2, N+1):
    DP.append([DP[i-1][0] + DP[i-1][1], DP[i-1][0]])
print(sum(DP[N]))
