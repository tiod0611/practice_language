'''
comment

입력받은 정수n을 reverse 한 뒤 배열로 만드는 문제.
정수를 문자열로 바꾸면 reverse와 배열화를 쉽게 할 수 있다.

'''

def solution(n):

    reversed_n = str(n)[::-1]
    answer = [int(i) for i in reversed_n]

    return answer

if __name__=='__main__':
    n = 12345
    result = solution(n)
    print(result)