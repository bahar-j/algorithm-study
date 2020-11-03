# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # i == 체크할 index , i+1 == 인용 횟수
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] - (i + 1) >= 0:
            answer = i + 1
            break

    return answer