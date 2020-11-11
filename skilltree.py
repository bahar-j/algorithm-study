# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        skill_order = list(skill)
        done = True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill_order:
                if skill_trees[i][j] != skill_order[0]:
                    done = False
                    break
                else:
                    del skill_order[0]
            else:
                continue
        if done:
            answer += 1

    return answer