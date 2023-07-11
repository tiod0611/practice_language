'''
comment
v2를 풀고 단순히 '짝'이 맞는지라는 측면에서 괄호의 갯수를 새는 방법을 떠올려봤다.
괄호의 갯수를 각각 count한 다음 같으면 True를 다르면 False를 출력하도록 했다..

그런데 프로그래머스에서는 3가지 testcase에 대해서 오답이 발생했다.
당연하다. 
"())(()" 이런 케이스에 대해서는 괄호의 수는 일치하지만, 3,4번 괄호가 어긋나있기 때문이다.
v2의 방법은 단순히 짝을 찾는 것이 아니라 ()의 순서를 고려하는 점에서 차이가 나는 것이다. 
'''


def solution(s):
    if s[0] == ')':
        return False
    leftCount = s.count('(')
    rightCount = s.count(')')
    return leftCount == rightCount
    
if __name__=='__main__':
    s = "())(()"
    result = solution(s)
    print(result)

    