def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    total_value = 0
    for index in range((len(sorted_score)//m)+1):
        box = sorted_score[index*m:(index+1)*m]
        if len(box) <m:
            break
        value = min(box) * m
        total_value += value

    return total_value

def solution_1(k, m, score):

    value = 0
    sorted_score = sorted(score, reverse=True)
    boxes = [sorted_score[i:i+m] for i in range(0, len(sorted_score), m)]
    for box in boxes:
        if len(box) < m:
            break
        value += min(box)*m

    return value

def solution_2(k, m, score):
    value = 0
    sorted_score = sorted(score, reverse=True)
    for i in range(m-1, len(score), m):
        value += sorted_score[i] * m
    
    return value

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
answer = solution_2(k, m, score)
print(answer)