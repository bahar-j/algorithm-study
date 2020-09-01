
def make_one(num, answer):
    tmp_answer = []

    # 2의 배수인 경우
    if(num % 2 == 0):
        # 2로 나눈 후(횟수 + 1) 부분 해 사용
        tmp_answer.append(answer[(num // 2) - 1] + 1)
    # 3의 배수인 경우
    if(num % 3 == 0):
        tmp_answer.append(answer[(num // 3) - 1] + 1)
    # default: 이전 숫자의 부분 해 + 1
    if(num >= 2):
        tmp_answer.append(answer[num-2] + 1)
    elif(num == 1):
        tmp_answer.append(0)

    return min(tmp_answer)

num = int(input())
answer = []

# 1부터 부분 해 모두 구하기
for i in range(1, num+1):
    answer.append(make_one(i, answer))

# 부분 해 배열의 마지막 원소가 최종 해
print(answer[num-1])


