
'''
풀이
1. n이 2의 지수로 표현할 때, 지수 자리 숫자를 알아야함.
2. n = 2^c라고 할 때, 2^c을 기준으로 a와 b의 범위가 나뉠 때까지 시도함
3. c에서 2번 과정을 반복할 때마다 c=c-1을 하고, a와 b의 범위가 나뉘는 곳에서 정답이 나옴.

==
알고리즘은 틀리지 않았으나, 프로그래머스 체점에서 계속해서 시간초과가 발생함. 
내가 사용한 방법에서 log2를 계산하는데 추가적인 시간이 발생하기 때문으로 생각함.
아래 solution2는 인터넷에 있는 풀이 중 하나다. 이 방법을 보면 log를 사용하지 않고, 규칙성을 발견해서 풀이했다.

흠 좀 더 고민이 필요하다. 
'''

def log2(x):
    n = 0
    while x > 1:
        x /= 2
        n += 1
    return n

def solution(n, a, b):
    c = log2(n) # 2의 지수 자리 수
    a, b = (b, a) if a > b else (a, b)
    while True:
        n = n // 2
        if (a <= n) and (b > n):
            return c
        c -= 1

def solution2(n,a,b): 
	answer = 0
	while a != b: 
		answer += 1
		a, b = (a+1)//2, (b+1)//2
	return answer

if __name__=="__main__":
    n, a, b = 2**19, 636, 1415
    result = solution(n, a, b)
    result2 = solution2(n, a, b)
    print(result)
    print(result2)