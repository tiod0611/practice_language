'''
python의 bin().count() 메서드를 사용하면 간단히 해결되는 문제.

'''

def solution(n):
    count_one = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == count_one:
            return n

if __name__=='__main__':
    n = 78
    result = solution(n)
    print(result)