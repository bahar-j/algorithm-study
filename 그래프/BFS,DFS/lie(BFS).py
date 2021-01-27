# https://www.acmicpc.net/problem/1043
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
parties = {i: [] for i in range(1, M+1)} # 파티 별 사람 목록
people = {i: [] for i in range(1, N+1)} # 사람 별 파티 목록
checked = [False] * (N+1) # 확인한 사람
lie_available = [True] * (M+1)

tmp = list(map(int, input().split()))
n_truth = tmp[0]
if n_truth == 0:
    print(M)
else:
    people_know_truth = tmp[1:]

    for i in range(1, M+1):
        tmp = list(map(int, input().split()))
        party_people = tmp[1:]
        parties[i] = party_people
        for p in party_people:
            people[p].append(i)

    while people_know_truth:
        person = people_know_truth.pop()
        checked[person] = True
        visited_party = people[person]
        for party in visited_party:
            lie_available[party] = False
            for p in parties[party]:
                if not checked[p]:
                    people_know_truth.append(p)

    print(lie_available.count(True)-1)
