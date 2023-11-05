'''
comment

이 문제는 두가지 케이스를 고려하면서 틀린 사람과 틀린 순서를 반환하면 되는 문제
1. 중복 단어는 이전에 나온 단어를 stack에 쌓고 지금 단어가 포함되어 있는지 살피면 된다.
2. 끝말인지 확인하는 방법은 stack의 마지막 단어의 마지막 글자와 현재 단어의 첫글짜를 비교하면 된다.
3. 틀린 사람을 구하는 방법은 현재 단어 번호를 참가자로 나눈 나머지로 한다. 이때 나머지가 0이면 n번이 틀린 사람이다.
4. 틀린 사람의 순서는 단어 순서를 참가자로 나누고 반오림 하여 구했다. 

'''

import math
def solution(n, words):
    stack = []
    
    for i, word in enumerate(words, start=1):
        who = i%n if (i%n) != 0 else n
        order = math.ceil(i / n)
        # 중복된 단어인지 확인
        if word in stack :
            return [who, order]
        # 끝말을 잘 잇고 있는지 확인
        elif i > 1 and stack[-1][-1] != word[0]: 
            print(stack[-1], word)
            return [who, order]
        
        else: 
            stack.append(word)
    return [0, 0]

if __name__ == '__main__':
    words = ["hello", "one", "even", "never", "now", "world", "draw"]
    n = 2
    result = solution(n, words)
    print(result)
        