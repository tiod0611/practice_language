'''
팰린드롬수
https://www.acmicpc.net/problem/1259

입력
입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

출력
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
'''

while True:
    word = input()
    if word == '0':
        break
    reversedWord = word[::-1]
    if word == reversedWord:
        print("yes")
    else:
        print("no")