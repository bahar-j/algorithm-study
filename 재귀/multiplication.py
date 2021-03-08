# https://www.acmicpc.net/problem/1629

def power(a, b):
    if b == 1:
        return a % C
    else:
        tmp = power(a, b//2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C

A, B, C = map(int, input().split())

print(power(A, B))
