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

def solution_1(numbers, k):
    
    numbers = sorted(list(set(numbers)), reverse=True)
    n = len(numbers)
    print(numbers)
    print(n, k)
    first = 0
    second = 1
    third = 2
    for _ in range(k):
        print(numbers[first] , numbers[second] , numbers[third])
        answer = numbers[first] + numbers[second] + numbers[third]
        
        print(answer)
        print(first, second, third)
        if third < n-1: # third가 n보다 작으면 1씩 계속 증가
            third += 1
        else:   # third가 n보다 크다면
            second += 1 # second을 하나 증가시키고
            third = second + 1 # third index를 second보다 +1 
            if second > n-2: # second가 마지막 -1 index에 도달했다면
                first += 1 # first를 하나 증가시키고
                second = first + 1 # second와 third 초기화
                third = second + 1
                if first > n-3:
                    assert print('Somthing is wrong!')
        # print(numbers[first] + numbers[second] + numbers[third] )
    return answer

# 조건에 모든 경우의 수를 구하라는 조건이 있음.
# index가 중복되어서는 안됨. 
# 반복문을 제어할 때 index가 겹치지 않게 조정할 것. 
def solution_2(numbers, k): 
    numbers = list(set(numbers))
    answers = []
    for i in range(len(numbers[:-2])):
        for j in range(i+1, len(numbers[i+1:-1])):
            for l in range(j+1, len(numbers[j+1:])):
                answers.append(numbers[i] + numbers[j] + numbers[l])
                print(numbers[i], numbers[j], numbers[l])
    result = sorted(answers, reverse=True)
    print(result)
    return result[k-1]

def solution_3(numbers, k):
    numbers = list(set(numbers))
    summation = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for m in range(j+1, n):
                summation.append(numbers[i] + numbers[j] + numbers[m])
    result = sorted(summation, reverse=True)[k-1]
    return result

print(solution_3(numbers, k))