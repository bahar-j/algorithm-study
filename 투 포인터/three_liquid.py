# https://www.acmicpc.net/problem/2473
import sys

N = int(input())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()
min_sum = float('inf')
picked = [0] * 3

for fixed_pointer in range(N-2):
    left, right = fixed_pointer + 1, N - 1
    while left < right:
        current_sum = liquids[fixed_pointer] + liquids[left] + liquids[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            picked[0] = fixed_pointer
            picked[1] = left
            picked[2] = right

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            print(liquids[fixed_pointer], liquids[left], liquids[right])
            sys.exit(0)

for idx in picked:
    print(liquids[idx], end=' ')


