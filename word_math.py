# https://www.acmicpc.net/problem/1339

import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
words = []
alphabets = defaultdict(int)
sum = 0

for _ in range(N):
    tmp = input().rstrip()
    for i in range(len(tmp)):
        ten = 10**(len(tmp)-1-i)
        alphabets[tmp[i]] += 1 * ten
    words.append(tmp)

sorted_alphabets = sorted(alphabets.items(), key=(lambda x: x[1]), reverse=True)

start = 9
for a in sorted_alphabets:
    alphabets[a[0]] = start
    start -= 1

for word in words:
    for i in range(len(word)):
        ten = 10**(len(word)-1-i)
        sum += alphabets[word[i]]*ten

print(sum)