# https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0


def DFS(numbers, value, idx, target):
    global answer

    if (idx == len(numbers)) and (value == target):
        answer += 1
        return
    if idx == len(numbers):
        return

    now = numbers[idx]

    DFS(numbers, value + now, idx + 1, target)
    DFS(numbers, value - now, idx + 1, target)


def solution(numbers, target):
    global answer

    DFS(numbers, 0, 0, target)

    return answer