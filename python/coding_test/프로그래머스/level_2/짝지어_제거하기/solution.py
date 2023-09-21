'''
comment

동일한 문자를 탐색할 때 stack을 사용해 같은 문자가 있는지 확인한다.
stack에 들어온 문자와 현재 문자를 비교하게 된다.
나란히 오는 문자가 있으면 stack에서 해당 문자를 제거하게 된다.
그렇게 지워진 문자열이 나란한 쌍이 연속되면 stack은 결국 비게 된다.
만약 문자가 하나라도 나란히 오지 못하면 stack은 비지 못하고 1을 반환한다. 
'''

def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:  # stack이 비어있지 않다면 stack에 있는 문자와 현재 문자를 비교해서 똑같으면
            stack.pop()  # 마지막 요소 제거
        else:
            stack.append(char) 
    
    return 0 if stack else 1
        
if __name__=='__main__':
    s = 'baabaa'
    result = solution(s)
    print(result)