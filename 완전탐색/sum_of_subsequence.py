# https://www.acmicpc.net/problem/1182
from sys import stdin

def bruteforce(parent, children, sum):
    global count

    sum += parent
    if sum == S:
        count += 1
    if len(children) < 1:
        return

    for i in range(len(children)):
        bruteforce(children[i], children[i+1:], sum)

input = stdin.readline
N, S = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0

for i in range(len(sequence)):
    sum = 0
    bruteforce(sequence[i], sequence[i+1:], sum)

print(count)