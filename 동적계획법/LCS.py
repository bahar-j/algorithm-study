import sys

word1 = str(sys.stdin.readline().strip())
word2 = str(sys.stdin.readline().strip())

LCS = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

for j in range(1, len(word1)+1):
    for i in range(1, len(word2)+1):
        if word1[j-1] == word2[i-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[-1][-1])