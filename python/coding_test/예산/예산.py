def solution(d, budget):
    answer, summation = 0, 0
    for i in sorted(d):
        summation += i
        if summation > budget:
            break
        answer += 1
    return answer