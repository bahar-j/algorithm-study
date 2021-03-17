# https://www.acmicpc.net/problem/11726

# DP[i] = DP[i-2] + DP[i-1]
# i-2에 누워있는 타일 2개
# i-1에 서있는 타일 1개

N = int(input())
DP = [0, 1, 2]

if N <= 2:
    print(DP[N])
else:
    for i in range(3, N+1):
        DP.append(DP[i-2] + DP[i-1])
    print(DP[-1]%10_007)