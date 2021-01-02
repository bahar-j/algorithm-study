# https://www.acmicpc.net/problem/4948

import math

def get_num_prime(num):
    is_prime = [True] * (num + 1)
    is_prime[1] = False

    sqrt_n = int(math.sqrt(num)) + 1
    for i in range (2, sqrt_n):
        if (is_prime[i]):
            for j in range(i**2, num + 1, i):
                is_prime[j] = False

    return is_prime[num//2 + 1:].count(True)

answer = []

while True:
    num = int(input())
    if num == 0:
        break
    answer.append(get_num_prime(num * 2))

for i in range(len(answer)):
    print(answer[i])

