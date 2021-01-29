# https://www.acmicpc.net/problem/1107

min_cnt = float('inf')
N = 0
btn_set = {i for i in range(0, 10)}

def bruteforce(clicked_num):
    global min_cnt, N, btn_set

    for btn in btn_set:
        tmp_num = clicked_num + str(btn)
        print(tmp_num)
        min_cnt = min(min_cnt, abs(N - int(tmp_num)) + len(tmp_num)) # 원래 숫자보다 자릿수가 적은 조합들도 다 비교(어차피 걸러짐)

        if len(tmp_num) < 6: # 고장나지 않은 버튼들의 조합 중 길이 6이하의 모든 조합을 확인
            bruteforce(tmp_num)


def main():
    global min_cnt, N, btn_set

    N = int(input())
    n_broken = int(input())

    min_cnt = min(min_cnt, abs(100-N)) # -, + 버튼만을 이용해 이동하는 경우
    btn_set -= set(map(int, input().split())) if n_broken else set()

    bruteforce('') if n_broken < 10 else '' # 숫자 버튼을 눌러서 이동하는 경우
    print(min_cnt)

main()