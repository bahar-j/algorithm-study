# https://www.acmicpc.net/problem/9663
# 시간 초과 !

def is_right_place(row, column):
    for i in range(column):
        if place[i] == row:
            return False
        if abs(row - place[i]) == abs(column - i):
            return False
    return True


def DFS(row, column):
    global count

    if not is_right_place(row, column):
        return

    place[column] = row

    if column == N-1:
        count += 1
        # print(place)
        return

    for new_row in range(N):
        if is_right_place(new_row, column+1):
            DFS(new_row, column+1)


N = int(input())
count = 0
place = [0] * N

for row in range(N):
    DFS(row, 0)

print(count*2)
