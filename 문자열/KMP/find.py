# https://www.acmicpc.net/problem/1786
# 예시 & 반례는 다 통과하는데 통과 못함

import sys

def make_table(target_str):
    table = [0]
    j = 0
    for i in range(1, len(target_str)):
        # j가 0이 될 때까지 감소시키며 타겟 문자열과 같아질 수 있는지 확인
        while (j != 0) and (target_str[i] != target_str[j]):
            j -= 1
        if target_str[i] == target_str[j]:
            j += 1
            table.append(j)
        else:
            table.append(0)
    return table

def KMP(target_str, search_str, table):
    count = 0
    place = []
    target_idx = 0
    for search_idx in range(len(search_str)):
        if (target_str[target_idx] != search_str[search_idx]) and target_idx == 0:
            continue
        if (target_str[target_idx] == search_str[search_idx]):
            if target_idx == len(target_str) - 1:
                place.append(search_idx - len(target_str) + 2)
                target_idx = table[target_idx]
                count += 1
            else:
                target_idx += 1
        else:
            target_idx = table[target_idx - 1] + 1
    return count, place

def init():
    search_str = sys.stdin.readline().replace("\n","")
    target_str = sys.stdin.readline().replace("\n","")

    if not target_str:
        print(0)
        return

    table = make_table(target_str)
    count, place = KMP(target_str, search_str, table)
    print(count)

    for i in place:
        print(i, end=" ")

init()


