# https://www.acmicpc.net/problem/11052

from sys import stdin

N = int(input())
card_deck = list(map(int, stdin.readline().split()))
D = [0] * (N+1)     # 인덱스에 해당하는 카드 수를 갖기 위해 지불해야할 최대 금액
D[1] = card_deck[0]

for i in range(2, N+1):
    candidates = []
    candidates.append(card_deck[i-1])
    for j in range(i-1, 0, -1):
        # if D[j]+D[i-j] in candidates:
        #     break
        candidates.append(D[j]+D[i-j])
    D[i] = max(candidates)

print(D[-1])