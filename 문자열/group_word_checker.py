from sys import stdin

N = int(stdin.readline().strip())
count = 0

for _ in range(N):
    is_group = True
    recent = ''
    prev = []
    word = list(stdin.readline().strip())
    while is_group and word:
        now = word.pop()
        if (now != recent) and (now in prev):
            is_group = False
        recent = now
        prev.append(now)
    if is_group:
        count += 1

print(count)
