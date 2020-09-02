# 시간 초과 뜸 !

import sys

N, SIZE = map(int, sys.stdin.readline().split())
stuffs = list()
in_out = [0 for _ in range(N)]
max_value = [0]

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    effectiveness = v / w
    stuffs.append([w, v, effectiveness])

stuffs_sorted = sorted(stuffs, key=lambda x: x[2])


def frac_knapsack(depth, weight_left):
    on_estimation = stuffs[depth:]
    value = 0

    for j in range(len(stuffs)):
        if stuffs_sorted[j] in on_estimation:
            if weight_left - stuffs_sorted[j][0] >= 0:
                value += stuffs_sorted[j][1]
            else:
                value += stuffs_sorted[j][1] * (weight_left/stuffs_sorted[j][0])

    return value


def knapsack(depth, weight_left, in_out, value_now):

    if (depth == N) or (weight_left <= 0):
        return

    # 현재 depth의 값을 넣는 경우
    if weight_left - stuffs[depth][0] >= 0:
        estimated_profit = frac_knapsack(depth+1, weight_left-stuffs[depth][0])
        if max_value[0] < (value_now + stuffs[depth][1] + estimated_profit):
            in_out_copy = in_out[:]
            in_out_copy[depth] = 1
            max_value[0] = max(max_value[0], value_now + stuffs[depth][1])
            knapsack(depth+1, weight_left - stuffs[depth][0], in_out_copy, value_now + stuffs[depth][1])

    # 현재 depth의 값을 넣지 않는 경우
    estimated_profit = frac_knapsack(depth+1, weight_left)
    if max_value[0] < value_now + estimated_profit:
        in_out_copy = in_out[:]
        in_out_copy[depth] = 0
        knapsack(depth+1, weight_left, in_out_copy, value_now)


knapsack(0, SIZE, in_out, 0)

print(max_value[0])

