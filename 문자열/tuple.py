# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

def solution(s):
    answer = []

    s = s[2:-2]
    tuple = s.split('},{')

    for i in range(len(tuple)):
        tuple[i] = tuple[i].split(',')

    tuple = sorted(tuple, key=len)

    for m in range(len(tuple)):
        now = tuple[m][0]
        for n in range(len(tuple)):
            if now in tuple[n]:
                tuple[n].remove(now)
            if n == m and len(tuple[n]) == 0:
                answer.append(int(now))

    return answer