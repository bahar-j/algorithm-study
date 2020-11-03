# https://www.acmicpc.net/problem/1931

from sys import stdin

num_meeting = int(stdin.readline())
meetings = []
prev_end = 0
meeting_available = 0

# 다차원 배열 만들기
for i in range (num_meeting):
    start, end = map(int, stdin.readline().split())
    meetings.append([start, end])

# 정렬
meetings = sorted(meetings, key=lambda x:(x[1],x[0]))

# 가능한 회의 갯수 계산
for i in range (num_meeting):
    if ( meetings[i][0] >= prev_end ):
        meeting_available += 1
        prev_end = meetings[i][1]

print(meeting_available)