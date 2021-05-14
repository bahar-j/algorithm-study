# https://www.acmicpc.net/problem/1717
# 원래 유니온 파인드는 자기 바로 위의 부모를 가지고 있는 형태
# 이 문제처럼 같은 집합에 속하는지 알기만 하면 되는 경우에는
# 모든 노드가 최종 조상을 가지면 됨

import sys
sys.setrecursionlimit(10 ** 7)

def find_parent(x):
    if parents[x] == x:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union(a, b):
    # find_parent하면 a,b의 부모는 이미 바뀐 상태
    # * a,b의 최종 조상을 둘 중 더 작은 최종 조상으로 바꿔줘야함!! *
    parent_a, parent_b = find_parent(a), find_parent(b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

input = sys.stdin.readline
N, M = map(int, input().split())
parents = [i for i in range(N+1)]

for _ in range(M):
    type_, a, b = map(int, input().split())
    if type_ == 0:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
