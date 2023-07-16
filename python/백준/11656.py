'''

1. 접미사 배열을 만든다
2. 사전별 우선순위로 정렬한다
3. 정렬된 배열에서 첫 글자가 같아 같은 레벨에 속한 단어는 그 다음 자리 글자의 크기를 비교해야 한다.
근데 파이썬의 정렬은 이걸 알아서 해준다. 
'''

s = input()

suffixs = [s[-i:] for i in range(1, len(s)+1)]
suffixs = sorted(suffixs)

for i in suffixs:
    print(i)