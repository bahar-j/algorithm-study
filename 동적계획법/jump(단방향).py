import sys
# DFS + DP로 풀면 시간 초과남

input = sys.stdin.readline
N = int(input())
map = []
DP = [[0 for _ in range (N)] for _ in range (N)]
DP[0][0] = 1
for _ in range(N):
    map.append(list(input().split()))

def main():
    for i in range(N):
        for j in range(N):
            jump = int(map[i][j])
            if jump == 0:
                return
            if 0 <= i+jump < N:
                DP[i+jump][j] += DP[i][j]
            if 0 <= j+jump < N:
                DP[i][j+jump] += DP[i][j]

main()
print(DP[-1][-1])