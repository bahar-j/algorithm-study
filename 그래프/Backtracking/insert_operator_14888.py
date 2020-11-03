# https://www.acmicpc.net/problem/14888

import sys

N = int(input())
nums = [int(x) for x in sys.stdin.readline().split()]
num_operator = [int(x) for x in sys.stdin.readline().split()]
output = list()

maxmin = [-1000000000, 1000000000]
depth = 0


def calculate(next_num, idx, pre_total):

    if idx == 0:
        return pre_total + next_num

    elif idx == 1:
        return pre_total - next_num

    elif idx == 2:
        return pre_total * next_num

    else:
        if pre_total < 0:
            return -(-(pre_total) // next_num)
        return pre_total // next_num


def dfs(depth, num_operator, pre_total):

    if depth == N-1:
        maxmin[0] = max(maxmin[0], pre_total)
        maxmin[1] = min(maxmin[1], pre_total)
        return

    depth += 1
    next_num = nums[depth]

    for idx in range(4):
        if num_operator[idx] > 0:
            operator_copy = num_operator[:]
            operator_copy[idx] -= 1
            cur_total = calculate(next_num, idx, pre_total)
            dfs(depth, operator_copy, cur_total)


dfs(depth, num_operator, nums[0])

print(maxmin[0], maxmin[1])