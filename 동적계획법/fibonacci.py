
def generate_fibo(pos):
    # 규칙에서 벗어나는 값 먼저 넣기
    fibo = [0,1]
    
    # 규칙에 맞게 피보나치 배열 생성
    for i in range(2, pos+1):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[pos]

pos = int(input())
answer = generate_fibo(pos)
print(answer)

