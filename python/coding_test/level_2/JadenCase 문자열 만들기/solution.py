'''
comment 
각 단어의 첫 문자열을 대문자로 만들면 되는 문제.
파이썬의 경우 capitalize()메서드를 사용하면 문자열의 첫 글자를 대문자로 바꿔준다.
이 메서드를 사용할 때 문자열의 종류-영어, 숫자, 한글 등-을 고려할 필요가 없어 매우 쉽게 해결이 가능하다.
문자열에 속한 모든 단어에 대해서 capitalize()를 진행해야 하므로 
1. 문자열을 ' '를 기준으로 리스트로 변환
2. 각 원소에 대해서 capitalize() 진행
3. 다시 하나의 문자열로 join을 수행
하면 된다.
'''

def solution(s):
    s_list = s.split(" ")
    cap_s_list = [word.capitalize() for word in s_list]
    answer = ' '.join(cap_s_list)
    return answer


if __name__=="__main__":
    s = "3people unFollowed me"
    answer = solution(s)
    print(answer)