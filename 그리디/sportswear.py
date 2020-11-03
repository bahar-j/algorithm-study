# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n - len(lost)
    # 잃어버렸으면서 여분이 있는 학생 제거
    for k in range(1, n + 1):
        if (k in lost) and (k in reserve):
            lost.remove(k)
            reserve.remove(k)
            answer += 1

    for j in range(2):
        i = 0
        while (i != len(lost)) and (answer != n):
            now = lost[i]

            # 왼쪽 오른쪽 학생이 다 여분 있는 경우는 1회 보류
            if (now - 1 in reserve) and (now + 1 in reserve) and (j == 0):
                i += 1
                continue
            # 왼쪽 학생만 있는 경우
            elif now - 1 in reserve:
                lost.remove(now)
                reserve.remove(now - 1)
                answer += 1
            # 오른쪽 학생만 있는 경우
            elif now + 1 in reserve:
                lost.remove(now)
                reserve.remove(now + 1)
                answer += 1
            # 양쪽 다 없는 경우
            else:
                i += 1
                continue

    return answer