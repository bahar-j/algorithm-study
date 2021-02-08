# https://www.acmicpc.net/problem/17136
# 10 X 10이라 그래프 자체를 수정하고 매번 1인 인덱스를 새로 찾는게 나은데
# 1인 위치를 리스트로 유지해주려고 했더니 시간 초과남

# 붙일 수 있는지 확인하는 부분에서 가로 세로 너비 더했을 때
# 10 넘는지 확인해서 바로 리턴 안해도 시간 초과남
import sys

def can_stick(r, c, width):
    tmp = []
    is_available = True
    if r + width > 10 or c + width > 10:
        return False, tmp
    for i in range(r, r+width):
        for j in range(c, c+width):
            if paper[i][j] == 1:
                tmp.append([i, j])
            else:
                is_available = False
                break
    return is_available, tmp

def find_idx():
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                return i, j

def update(spaces, to_):
    for s in spaces:
        paper[s[0]][s[1]] = to_

def bruteforce(remain, cnt):
    global answer

    if answer != -1 and cnt > answer:
        return

    if remain == 0:
        if answer == -1:
            answer = cnt
        else:
            answer = min(answer, cnt)
        return

    r, c = find_idx()

    for width in range(5, 0, -1):
        if num[width] > 0:
            flag, spaces = can_stick(r, c, width)
            if flag:
                num[width] -= 1
                update(spaces, 0)
                bruteforce(remain-len(spaces), cnt + 1)
                update(spaces, 1)
                num[width] += 1


input = sys.stdin.readline
paper = []
answer = -1
remain = 0
num = {i: 5 for i in range(1, 6)}

for i in range(10):
    tmp = input().split()
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
        if tmp[j] == 1:
            remain += 1
    paper.append(tmp)

if remain != 0:
    bruteforce(remain, 0)
    print(answer)
else:
    print(0)