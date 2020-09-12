
LINE = int(input())
triangle = []
P = []
temp = []

for i in range (LINE):
    element = input()
    triangle.append(element.split())

# 밑에서부터 탐색하기 위해 뒤집어줌
triangle.reverse()

# P[0][N]의 답은 자기 자신
P.append(triangle[0])

MAX = LINE-1

for i in range(1, LINE): # 행
    row = []
    for j in range(0, MAX): # 열
        temp.append(int(P[i-1][j]) + int(triangle[i][j]))
        temp.append(int(P[i-1][j+1]) + int(triangle[i][j]))
        row.append(max(temp))
        temp.clear()
    P.append(row)
    MAX -= 1

print(P[LINE-1][0])