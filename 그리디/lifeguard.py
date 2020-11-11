# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort()
    left_idx = 0
    right_idx = len(people) - 1

    while True:
        # 한 사람 남은 경우
        if left_idx == right_idx:
            answer += 1
            break
        # 남은 사람이 없는 경우
        if left_idx > right_idx:
            break
        # 두명이 탈 수 있는 경우
        if people[left_idx] + people[right_idx] <= limit:
            left_idx += 1
            right_idx -= 1
            answer += 1
        # 한명만 탈 수 있는 경우
        else:
            right_idx -= 1
            answer += 1

    return answer