# https://www.acmicpc.net/problem/2133

# DP(4) = DP(2)*3 + DP(0)*2
# DP(6) = DP(4)*3 + DP(2)*2 + DP(0)*2
# DP(8) = DP(6)*3 + DP(4)*2 + DP(2)*2 + DP(0)*2

def count(n):
    if n % 2 == 0:
        DP[n] = DP[n-2] * 3
        for j in range(4, n+1, 2):
            DP[n] += DP[n-j]*2

N = int(input())
DP = [0] * (N+1)
DP[0] = 1
if N >= 2:
    DP[2] = 3
    
if N >= 4:
    for i in range(4, N+1):
        count(i)

print(DP[N])



