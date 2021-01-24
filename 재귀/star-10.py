# https://www.acmicpc.net/problem/2447
import sys

def insert_pattern(prev_G, k):
    N = 3**k
    jump = 3**(k-1)
    G = [[0] * N for _ in range(N)]


    for m in range(3):
        for n in range(3):
            for i in range(jump*m, jump*m + N//3):
                for j in range(jump*n, jump*n + N//3):
                    if m == 1 and n == 1:
                        G[i][j] = 0
                    else:
                        G[i][j] = prev_G[i-jump*m][j-jump*n]

    if N == NUM:
        print_pattern(G)
        return
    else:
        insert_pattern(G, k+1)


def print_pattern(final):
    for i in range(len(final)):
        tmp = ''
        for j in range(len(final)):
            if final[i][j] == 0:
                tmp += ' '
            else:
                tmp += '*'
        print(tmp)



NUM = int(sys.stdin.readline())

graph = [[1,1,1],[1,0,1],[1,1,1]]

if NUM == 3:
    print_pattern(graph)
else:
    insert_pattern(graph, 2)

# 111
# 101
# 111
# 배열 크기 3

# 111 111 111
# 101 101 101
# 111 111 111
# 111 000 111
# 101 000 101
# 111 000 111
# 111 111 111
# 101 101 101
# 111 111 111
# 배열 크기 9

# 배열 크기 27






