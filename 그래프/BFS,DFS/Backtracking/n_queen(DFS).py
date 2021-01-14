# https://www.acmicpc.net/problem/9663
# 시간 초과 : !첫 줄 for 문 돌면서 시작해주는 것 하지 않기!

def is_right_place(row, column):
    for i in range(column):
        if place[i] == row:
            return False
        if abs(row - place[i]) == abs(column - i):
            return False
    return True


def DFS(column):
    global count

    if column == N:
        count += 1
    else:
        for row in range(N):
            if is_right_place(row, column):
                place[column] = row
                DFS(column+1)
                # place[column] = 0 => 안해주면 기존의 리스트에 덮어씀

N = int(input())
count = 0
place = [0] * N

DFS(0)

print(count)
