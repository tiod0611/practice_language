
'''
이 문제를 보고 3가지 풀이 방법이 떠올랐고, 각 순서대로 접근해볼 생각이다.

1. 문자열 검사 방법
2. Stack으로 짝 찾기 방법
3. 제귀함수 방법

comment
주어진 문자열 s에서 "()"로 짝지어진 문자 제거를 반복적으로 시도한다.
문자열 제거를 시도할 때마다, 
남은 문자열이 없으면 True를 반환, 
"()" 문자가 없는데 문자열 길이가 0이 아니면 False를 반환
하는 방법이다.

이 방법을 쓰면 모든 케이스에 대해서 문제없이 해결이 가능하다.
하지만 무한루프를 사용해서인지, 효율성 테스트에서 통과하지 못한다.

'''
def solution(s):
    
    while True:
        if '()' not in s:
            if len(s) == 0:
                return True
            else:
                return False
            
        s = s.replace('()','')

    
if __name__=='__main__':
    s = ")()("
    result = solution(s)

    print(result)

    


    
