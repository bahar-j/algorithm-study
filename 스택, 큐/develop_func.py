# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    now = 0

    while (progresses):
        while (progresses[0] < 100):
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        while (progresses):
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                now += 1
            else:
                answer.append(now)
                now = 0
                break
    answer.append(now)

    return answer