# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = -1
    DP = list()

    # 최솟값 1~8까지 전체 경우 탐색
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for op1 in DP[j]:
                for op2 in DP[-j - 1]:
                    numbers.add(op1 + op2)
                    numbers.add(op1 - op2)
                    numbers.add(op1 * op2)
                    if op2 != 0:
                        numbers.add(op1 // op2)

        if number in numbers:
            answer = i
            break

        DP.append(numbers)

    return answer


'''
i = 1
j -> (0, 0):

DP[0] = {5}
numbers = {5}
DP = [{5}] # 1번set

i = 2
j -> (0, 1):

DP[0] + DP[-1] = {5} (사칙연산) {5}
numbers = {55, 10, 0, 25, 1}
DP = [{5}, {55, 10, 0, 25, 1}] # 1번set, 2번set

i = 3
j -> (0, 2):
DP[0] + DP[-1] = {5} (사칙연산) {55,10,0,25,1} 
DP[1] + DP[-2] = {55,10,0,25,1} (사칙연산) {5}
DP = [{5}, {55, 10, 0, 25, 1}, {555, 1번set+2번set union 2번set+1번set}] # 1번set, 2번set, 3번set

'''

