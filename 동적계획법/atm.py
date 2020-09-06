from sys import stdin

def calculate_sum(n):
    sum = 0
    for i in range (n):
        for j in range (i+1):
            sum += line[j]
    return sum

num_people = int(stdin.readline())

line = list(map(int, stdin.readline().split()))
line.sort()
sum = calculate_sum(num_people)
print(sum)
