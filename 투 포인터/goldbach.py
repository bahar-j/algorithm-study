# https://www.acmicpc.net/problem/9020

from sys import stdin
import math

def answer(n, primes):
    prime_left = n // 2
    prime_right = prime_left
    for _ in range(5000): # 주어진 n의 범위 0~10000
        if primes[prime_left] and primes[prime_right]:
            return prime_left, prime_right
        prime_left -= 1
        prime_right += 1

def get_prime(n):
    is_prime = [True] * n # n은 짝수니까 소수 아님
    is_prime[0] = False
    is_prime[1] = False

    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if is_prime[i]:
            for j in range(i*2, n, i):
                is_prime[j] = False

    return is_prime


input = stdin.readline
TEST_CASE = int(input())
input_nums = []
max_num = 0

for _ in range(TEST_CASE):
    input_nums.append(int(input()))
    if input_nums[-1] > max_num:
        max_num = input_nums[-1]

# 가장 큰 수의 소수 구하기
primes = get_prime(max_num)

for num in input_nums:
   print(*answer(num, primes))



