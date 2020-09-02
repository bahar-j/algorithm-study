import sys
from itertools import combinations
from collections import deque

N = int(sys.stdin.readline().strip())
HEADCOUNT = N // 2
G = []
min_gap = [float('inf')]
member = []
start = ''
link = ''

for i in range(N):
    member.append(str(i))
    G.append([int(x) for x in sys.stdin.readline().split()])

combination_team = deque(list(map(','.join, combinations(member, HEADCOUNT))))
# ['1,2', '1,3', '1,4', '2,3', '2,4', '3,4']


def calculate_score(team):
    score = 0
    team_arr = team.split(',')  # ['1', '2', '3']
    combination_member = list(map(''.join, combinations(team_arr, 2)))
    # ['12', '13', '23']
    for k in range(len(combination_member)):
        now = combination_member[k]
        score += (G[int(now[0])][int(now[1])] + G[int(now[1])][int(now[0])])

    return score

for _ in range(len(combination_team)//2):
    start = combination_team.popleft()
    link = combination_team.pop()

    start_score = calculate_score(start)
    link_score = calculate_score(link)

    tmp = abs(start_score - link_score)
    min_gap[0] = min(tmp, min_gap[0])

    if min_gap[0] == 0:
        break

print(min_gap[0])
