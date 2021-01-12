# https://www.acmicpc.net/problem/10844

N = int(input())
MOD = 1000000000

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):  # N이 1일 때는 0이 올 수 없음
    dp[1][i] = 1

for m in range(2, N+1):
    for n in range(10):
        if n == 9:
            dp[m][n] = dp[m-1][n-1]
        elif n == 0:
            dp[m][n] = dp[m-1][n+1]
        else:
            dp[m][n] = dp[m-1][n-1] + dp[m-1][n+1]

print(sum(dp[N]) % MOD)



