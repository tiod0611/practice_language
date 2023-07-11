def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            answer.append(numbers[i]+j)
    
    answer = list(set(answer))
    return sorted(answer)