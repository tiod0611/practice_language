'''
뒤집힌 덧셈
https://www.acmicpc.net/problem/1357

입력
첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

X, Y = input().split(' ')
revX = int(X[::-1])
revY = int(Y[::-1])
sumRevXY = int(str(revX+revY)[::-1])
print(sumRevXY)