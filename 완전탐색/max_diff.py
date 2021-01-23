# https://www.acmicpc.net/problem/10819
from sys import stdin
import itertools

input = stdin.readline
N = int(input())
nums = list(map(int, input().split()))
permutation = list(itertools.permutations(nums))
max_sum = 0

for item in permutation:
    tmp = 0
    for i in range(len(item)-1):
        tmp += abs(item[i] - item[i+1])
    max_sum = max(max_sum, tmp)
print(max_sum)
