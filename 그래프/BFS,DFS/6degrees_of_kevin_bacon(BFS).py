# https://www.acmicpc.net/problem/1389

import sys
from collections import deque

def get_degree(from_):
    visited = [False] * (N+1)
    visited[from_] = True
    queue = deque()
    queue.append([from_, 1])

    while queue:
        now, degree = queue.popleft()
        adjacents = G[now]
        for a in adjacents:
            if not visited[a]:
                queue.append([a, degree+1])
                answer[from_][a] = degree
                visited[a] = True

input = sys.stdin.readline
N, M = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
answer = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    from_, to_ = map(int, input().split())
    G[from_].append(to_)
    G[to_].append(from_)

for i in range(1, N+1):
    get_degree(i)

answers = []# https://www.acmicpc.net/problem/1389

import sys
from collections import deque

def get_degree(from_):
    visited = [False] * (N+1)
    visited[from_] = True
    queue = deque()
    queue.append([from_, 1])

    while queue:
        now, degree = queue.popleft()
        adjacents = G[now]
        for a in adjacents:
            if not visited[a]:
                queue.append([a, degree+1])
                answer[from_][a] = degree
                visited[a] = True

input = sys.stdin.readline
N, M = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
answer = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    from_, to_ = map(int, input().split())
    G[from_].append(to_)
    G[to_].append(from_)

for i in range(1, N+1):
    get_degree(i)

answers = []
for i in range(1, N+1):
    answers.append((sum(answer[i]), i))

answers = sorted(answers, key=lambda x: (x[0], x[1]))
print(answers[0][1])
for i in range(1, N+1):
    answers.append((sum(answer[i]), i))

answers = sorted(answers, key=lambda x: (x[0], x[1]))
print(answers[0][1])