# https://www.acmicpc.net/problem/10819
from sys import stdin

def traverse(tmp, visited):
    if len(tmp) == N:
        calculate(tmp)
        return

    for i in range(len(nums)):
        if not visited[i]:
            tmp.append(nums[i])
            visited[i] = True
            traverse(tmp, visited)
            visited[i] = False
            tmp.pop()


def calculate(tmp):
    global max_sum
    sum = 0
    for i in range(len(tmp)-1):
        sum += abs(tmp[i] - tmp[i+1])
    max_sum = max(sum, max_sum)


input = stdin.readline
N = int(input())
nums = list(map(int, input().split()))
max_sum = 0

for i in range(len(nums)):
    visited = [False] * N
    tmp = [nums[i]]
    visited[i] = True
    traverse(tmp, visited)

print(max_sum)