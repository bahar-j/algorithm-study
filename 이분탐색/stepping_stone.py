# https://programmers.co.kr/learn/courses/30/lessons/64062
# 이분 탐색 기준 == 건널 수 있는 사람 수
import copy

def solution(stones, k):
    INF = 200_000_000
    left, right = 1, INF

    while left <= right:
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)
        for i in range(len(stones)):
            tmp[i] -= mid

        zero_in_a_row = 0
        check = False
        for j in range(len(stones)):
            if tmp[j] <= 0:
                zero_in_a_row += 1
            else:
                zero_in_a_row = 0

            if zero_in_a_row >= k:
                check = True
                break

        if check:
            right = mid - 1
        else:
            left = mid + 1

    return left