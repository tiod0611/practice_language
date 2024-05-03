# import sys
# sys.stdin=open('input.txt', 'rt')

n, k = map(int, input().split())

def solution(n, k):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)

    if len(divisor) < k:
        print(-1)
    else:
        print(divisor[k-1])

def solution_1(n, k):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt+=1
        if cnt == k:
            print(i)
            break
    else:
        print(-1)

solution_1(n, k)