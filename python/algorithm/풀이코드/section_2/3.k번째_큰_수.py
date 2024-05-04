import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

def solution(numbers, n, k):
    numbers = sorted(numbers, reverse=True)
    n -= 1
    first = 0
    second = 1
    third = 2
    for _ in range(k):
        answer = numbers[first] + numbers[second] + numbers[third]
        print(answer)
        if third < n: # third의 index보다 작으면 1씩 계속 증가
            third += 1
        else:   # third가 마지막 index보다 크다면
            second += 1 # second을 하나 증가시키고
            third = second + 1 # third 초기화
            if second > n-1: # second가 마지막 -1 index에 도달했다면
                first += 1 # first를 하나 증가시키고
                second = first + 1 # second와 third 초기화
                third = second + 1
        # print(numbers[first] + numbers[second] + numbers[third] )
    return answer

def solution_1(numbers, n, k):
    numbers = sorted(list(set(numbers)), reverse=True)
    first = 0
    second = 1
    third = 2
    for _ in range(k):
        answer = numbers[first] + numbers[second] + numbers[third]
        print(answer)
        if third < n: # third의 index보다 작으면 1씩 계속 증가
            third += 1
        else:   # third가 마지막 index보다 크다면
            second += 1 # second을 하나 증가시키고
            third = second + 1 # third 초기화
            if second > n-1: # second가 마지막 -1 index에 도달했다면
                first += 1 # first를 하나 증가시키고
                second = first + 1 # second와 third 초기화
                third = second + 1
        # print(numbers[first] + numbers[second] + numbers[third] )
    return answer

print(solution_1(numbers, n, k))