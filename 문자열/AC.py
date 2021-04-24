# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

def convert(l):
    l = l[1:-2]
    if not l:
        return []
    else:
        return list(l.split(','))

def convert_again(l):
    l = list(l)
    return '[' + ','.join(l) + ']'

input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    instruction = list(input().rstrip())
    n = int(input())
    nums = deque(convert(input()))
    reverse_direction = 1
    total_r_cnt = 0

    for i in instruction:
        if i == "R":
            reverse_direction *= -1
            total_r_cnt += 1
        elif i == "D":
            if nums:
                if reverse_direction == -1:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                nums = "error"
                break

    if total_r_cnt % 2 != 0 and nums != "error":
        nums.reverse()

    if nums != "error":
        print(convert_again(nums))
    else:
        print(nums)