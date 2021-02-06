# https://www.acmicpc.net/problem/16637

import sys

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "*":
        return num1 * num2
    if operator == "-":
        return num1 - num2

def bruteforce(before, idx):
    global result

    if idx >= N:
        result = max(result, before)
        return

    if idx < N-2:
        # 괄호 넣는 경우
        pair_result = calculate(int(formula[idx]), int(formula[idx+2]), formula[idx+1])
        new_num = calculate(before, pair_result, formula[idx-1])
        bruteforce(new_num, idx+4)
        # before 원래 값으로 돌아감

    # 괄호를 안 넣는 경우
    new_num = calculate(before, int(formula[idx]), formula[idx-1])
    bruteforce(new_num, idx+2)

input = sys.stdin.readline
N = int(input())
formula = list(input())
result = (-2)**31

if N == 1:
    print(int(formula[0]))
else:
    bruteforce(int(formula[0]), 2)
    print(result)

