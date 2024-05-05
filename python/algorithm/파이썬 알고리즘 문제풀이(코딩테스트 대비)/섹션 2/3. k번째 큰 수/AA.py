# import sys
# sys.stdin = open('input.txt', 'rt')

_, k = map(int, input().split())
numbers = list(map(int, input().split()))

def solution(numbers, k):
    # numbers = list(set(numbers))
    n = len(numbers)
    summation = set()
    for i in range(n):
        for j in range(i+1, n):
            for m in range(j+1, n):
                summation.add(numbers[i] + numbers[j] + numbers[m])
    result = sorted(list(summation), reverse=True)[k-1]
    return result

print(solution(numbers, k))