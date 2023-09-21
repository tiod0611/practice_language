'''
문자열 속에 p와 y의 갯수를 대소문자 구별없이 구하는 문제다.
파이썬의 경우 str().upper()나 str().lower()을 사용해 대소문자 통일 시킨 후 진행해도 된다.
근데 나는 반복문 두번을 사용하고 각각의 y와 p의 갯수를 구하였다. 
리스트 컴프리핸션을 사용하지 않고 그냥 반복문을 사용해서 한번에 하는 것도 가능하다.
'''

def solution(s):
    count_p = 0
    count_y = 0
    count_p = len([p for p in s if (p=="p") or (p=="P")])
    count_y = len([y for y in s if (y=="y") or (y=="Y")])
    
    return True if count_p == count_y else False

if __name__=="__main__":
    s = "Pyy"
    result = solution(s)
    print(result)