# import sys
# sys.stdin = open('input.txt', 'rt')

_, k = map(int, input().split())
numbers = list(map(int, input().split()))

def solution(numbers, k):
    
    numbers = sorted(list(set(numbers)), reverse=True)
    n = len(numbers)
    first = 0
    second = 1
    third = 2
    for _ in range(k):
        print(numbers[first] , numbers[second] , numbers[third])
        answer = numbers[first] + numbers[second] + numbers[third]

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

print(solution(numbers, k))