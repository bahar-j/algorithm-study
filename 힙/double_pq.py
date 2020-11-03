# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    answer = []
    queue = []
    idx = 0

    while idx < len(operations):
        tmp = operations[idx].split()
        cmd = tmp[0]
        data = int(tmp[1])
        if cmd == 'I':
            heapq.heappush(queue, data)
        else:
            if queue:
                if data == -1:
                    heapq.heappop(queue)
                else:
                    queue.pop(queue.index(max(queue)))
        idx += 1

    if not queue:
        return [0, 0]

    answer.append(max(queue))
    answer.append(queue[0])

    return answer