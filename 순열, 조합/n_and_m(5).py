# https://www.acmicpc.net/problem/15654

import sys
import copy

def permutation(pairs):
    global answer

    if len(pairs) == M:
        answer.append(copy.deepcopy(pairs))
        return

    for num in nums:
        if num not in pairs:
            pairs.append(num)
            permutation(pairs)
            pairs.pop()

input = sys.stdin.readline
N, M = map(int, input().split())
answer = []
nums = list(map(int, input().split()))

for num in nums:
    pairs = [num]
    permutation(pairs)

answer.sort()

for a in answer:
    print(' '.join(str(e) for e in a))