# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

def solution(n, times):
    answer = 0
    times.sort()
    left, right = 0, times[-1] * n

    while left <= right:
        people_available = 0
        mid = (left + right) // 2
        for time in times:
            people_available += mid // time
        if people_available >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

