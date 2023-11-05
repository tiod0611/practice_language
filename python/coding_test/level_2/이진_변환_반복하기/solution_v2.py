'''
comment

좀 더 간결한 이진수 변환 코드 버전
분리된 함수도 하나로 합쳤다.

'''


def remove_zero_and_transform_binary(s):
    '''
    문자열에서 0을 제거하고 제거된 0의 개수를 세는 함수.
    그리고 제거된 후의 문자열 길이를 이진수로 변환하는 함수.
    return: 
        binary_len, cnt_zero
    '''
    cnt_zero = s.count("0")
    s = s.replace("0", "")

    # 이진수 변환
    len_s = len(s)
    binary_len = ''
    while len_s > 0:
        binary_len = str(len_s % 2) + binary_len
        len_s //= 2
    
    return binary_len, cnt_zero

def solution(s):
    '''
    메인함수. 주어진 2진수 문자열을 1만 남을때까지 다음 작업을 반복한다.
    1. 주어진 문자열에서 0을 제거하고 제거된 0의 개수를 세는 작업과
    2. 그 결과 문자열의 길이를 이진수로 변환하는 작업을 한 번에 수행한다.
    제거된 0의 갯수를 구하고, 실행된 작업의 횟수를 구한다.
    return : 
        [n_iter, cnt_zero]
    '''
    n_iter = 0
    cnt_zero = 0
    while s != '1':
        n_iter += 1
        s, c_rmvd_zero = remove_zero_and_transform_binary(s)
        cnt_zero += c_rmvd_zero
    return [n_iter, cnt_zero]
