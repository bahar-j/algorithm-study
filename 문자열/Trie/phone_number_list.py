# https://www.acmicpc.net/problem/5052
# pypy로만 통과
from collections import defaultdict

N_TESTCASE = int(input())

for _ in range(N_TESTCASE):
    n_phone_number = int(input())
    tree = defaultdict(list)
    leaf_keys = []
    for i in range(n_phone_number):
        phone_number = str(input())
        for j in range(len(phone_number)):
            if j == len(phone_number) - 1:
                tree[phone_number[:j+1]].append('*')
                leaf_keys.append(phone_number[:j+1])
            else:
                tree[phone_number[:j+1]].append(phone_number[j+1])
    is_consistent = True
    for key in leaf_keys:
        if len(tree[key]) > 1:
            is_consistent = False
            break
    if is_consistent:
        print('YES')
    else:
        print('NO')
