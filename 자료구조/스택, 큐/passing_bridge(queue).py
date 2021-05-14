# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_on_bridge = deque([])
    truck_weights = deque(truck_weights)
    answer = 0
    sum_truck = 0

    while 1:

        # 총 경과 시간
        answer += 1

        if truck_on_bridge:
            # 다리에 트럭이 있다면, 트럭마다의 시간 증가
            # truck_on_bridge = ['weight,time',...]
            for i in range(len(truck_on_bridge)):
                tmp = truck_on_bridge[i].split(',')
                time_now = int(tmp[-1])
                updated_time = time_now + 1
                truck_on_bridge[i] = tmp[0] + ',' + str(updated_time)

            # 시간이 다 됐다면 다리에서 삭제
            tmp = truck_on_bridge[0].split(',')
            if int(tmp[-1]) == bridge_length + 1:
                tmp = truck_on_bridge.popleft().split(',')
                sum_truck -= int(tmp[0])

        if truck_weights:
            # 다리에 여유가 있다면, 새로운 트럭 추가
            if sum_truck + truck_weights[0] <= weight:
                time = 1
                tmp = truck_weights.popleft()
                sum_truck += tmp
                truck_on_bridge.append(str(tmp) + ',' + str(time))

        if not truck_on_bridge:
            break

    return answer