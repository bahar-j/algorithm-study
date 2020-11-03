# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def is_prime(num):
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    return (is_prime)


def solution(numbers):
    answer = 0
    prime_nums = list()

    # 자릿수 별 순열
    for j in range(1, len(numbers) + 1):
        p_list = list(map(''.join, permutations(numbers, j)))

        # 소수인지 확인
        for i in range(len(p_list)):
            if int(p_list[i]) not in prime_nums:
                if is_prime(int(p_list[i])):
                    prime_nums.append(int(p_list[i]))

    answer = len(prime_nums)

    return answer