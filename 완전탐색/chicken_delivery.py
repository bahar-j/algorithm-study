# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
G = []
chickens = []
houses = []
answer = float('inf')

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 2:
            chickens.append([i, j])
        elif tmp[j] == 1:
            houses.append([i, j])
    G.append(tmp)

for selected in combinations(chickens, M):
    town_chicken_dis = 0
    for house in houses:
        # 어떤 집에서 selected된 모든 치킨집까지의 거리를 구한 후, 최소인 거리를 치킨 거리로 선택하고 더해줌
        town_chicken_dis += min([abs(house[0]-i[0]) + abs(house[1]-i[1]) for i in selected])
        if answer <= town_chicken_dis:
            break
    answer = min(answer, town_chicken_dis)

print(answer)