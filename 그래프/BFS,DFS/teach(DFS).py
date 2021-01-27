# https://www.acmicpc.net/problem/1062
# pypy로 통과. 비트 마스킹으로 풀어야함
from sys import stdin, exit

def dfs(idx, cnt):
    global answer

    if cnt == K-5:
        can_read = 0
        for word in words:
            for w in word:
                if not learned[ord(w)-ord('a')]:
                    break
            else:
                can_read += 1

        answer = max(answer, can_read)
        return

    for i in range(idx, 26):
        if not learned[i]:
            learned[i] = True
            dfs(i, cnt+1)
            learned[i] = False

input = stdin.readline
N, K = map(int, input().split())

if K < 5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)

words = [set(input().rstrip()) for _ in range(N)]
learned = [False]*26
answer = 0

for a in ('a', 'c', 'i', 'n', 't'):
    learned[ord(a) - ord('a')] = True

dfs(0, 0)
print(answer)
