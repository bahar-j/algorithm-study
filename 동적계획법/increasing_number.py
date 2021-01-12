# https://www.acmicpc.net/problem/11057

N = int(input())
MOD = 10007

dp = [[0]*10 for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for m in range(2, N+1):
    for n in range(10):
        for l in range(n, 10):
            dp[m][n] += dp[m-1][l]

print(sum(dp[N]) % MOD)


