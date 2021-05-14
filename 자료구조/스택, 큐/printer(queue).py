# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)

    for j in range(len(priorities)):
        priorities[j] = str(priorities[j]) + str(j)
    answer = 0

    while (priorities):
        print(priorities)
        now = priorities.popleft()
        if not priorities:
            answer += 1
            return answer
        for i in range(len(priorities)):
            if int(priorities[i][0]) > int(now[0]):
                priorities.append(now)
                break
            if (i == len(priorities) - 1) and (int(priorities[i][0]) <= int(now[0])):
                answer += 1
                if int(now[1:]) == location:
                    return answer

    return answer