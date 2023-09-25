'''
comment

문자열에서 특정 문자를 제거하고 갯수를 세는 방법과
2진수 변환하는 방법을 복합적으로 물어보는 문제

    
'''

def remove_zero(s: str) -> tuple[str, int]:
    '''
    문자열에서 0을 제거한 결과와 제거된 0의 갯수를 반환하는 함수
    return: 
        rmvd_zero_s, cnt_zero
    '''
    rmvd_zero_s = s.replace("0","")
    cnt_zero = s.count("0")
    return rmvd_zero_s, cnt_zero

def transform_binary(digit: int) -> str:
    '''
    정수를 이진수로 변환하여 문자열로 함수 
    return:
        s
    '''
    s = ''
    while True:
        if digit < 2:
            s+=str(digit)
            s = s[::-1]
            return s
        rest = digit % 2
        digit = digit // 2
        s+=str(rest)

def solution(s: str) -> list:
    '''
    메인함수. 주어진 2진수 문자열을 1만 남을때까지 다음 작업을 반복한다.
    1. 주어진 문자열에서 0을 제거한뒤 제거된 0의 갯수를 센다.
    2. 남은 문자열 길이를 다시 2진수로 바꾸고 1의 작업으로 돌아간다.
    제거된 0의 갯수를 구하고, 실행된 작업의 횟수를 구한다.
    return : 
        [n_iter, cnt_zero]
    '''
    n_iter = 0
    cnt_zero = 0
    while True:
        n_iter += 1
        s, c_rmvd_zero = remove_zero(s)
        cnt_zero += c_rmvd_zero
        s = transfort_binary(len(s))
        if s == '1':
            return [n_iter, cnt_zero]
        


if __name__ == '__main__':
    s = "110010101001"
    result = solution(s)
    print(result)

