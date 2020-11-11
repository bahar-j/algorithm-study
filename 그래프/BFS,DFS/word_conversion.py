# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    while begin != target:
        for i in range(len(words)):
            duplicated = 0
            new_word = ''
            for j in range(len(words[i])):
                if words[i][j] == begin[j]:
                    duplicated += 1
                else:
                    new_word = words[i][:j] + target[j] + words[i][j + 1:]
            if len(begin) == duplicated + 1:
                begin = new_word
                answer += 1
                if begin == target:
                    break

    return answer