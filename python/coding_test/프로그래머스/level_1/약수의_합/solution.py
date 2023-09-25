'''
comment

기본적인 약수를 구하는 방법을 묻는 문제.
약수는 어떤 수를 나누어서 0으로 떨어지는 수의 집합이다.

이 문제의 테스트 케이스에서 1과 0을 입력으로 주어지기 때문에 이는 따로 처리했다.

'''


def solution(n):
    aliquot = []
    if n == 1 or n==0:
        return n
    for i in range(1, n+1):
        if i in aliquot:
            return sum(set(aliquot))
        if n%i == 0:
            aliquot.append(n/i)
            aliquot.append(i)
        
'''
comment

아래 코드는 ChatGPT에게 문제점과 개선사항을 물어본 결과다
몇가지 문제가 개선되었다.
1. 원래 코드는 list로 저장하고 나중에 set으로 형 변환을 했다. 이 과정은 불필요한 절차를 추가히기 때문에 처음부터 set 타입으로 선언하였다.
2. 약수를 구할 때 제곱근까지 반복하면 좋다는 사실은 알고 있었다. 그럼에도 in을 사용해서 이미 존재하는 원소까지만 반복하면 괜찮을 것이라 생각했다.
    하지만 in 연산은 모든 원소를 탐색하기 때문에 list의 크기가 커질 수록 연산 비용이 증가한다. 따라서 제곱근까지 반복하는 편이 바람직하다
'''
def solution(n):
    if n == 1 or n == 0:
        return n
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

if __name__=='__main__':
    n = 0
    result = solution(n)
    print(result)