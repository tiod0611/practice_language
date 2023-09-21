'''
comment

주어진 수 n의 배수를 n만큼 출력하면 되는 문제. 
list comprehension으로 쉽게 풀어낼 수 있따.
'''

def solution(x, n):
    answer = [x*i for i in range(1, n+1)]
    return answer