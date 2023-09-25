'''
명령 프롬프트
https://www.acmicpc.net/problem/1032

입력
첫째 줄에 파일 이름의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다. N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다. 파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.

출력
첫째 줄에 패턴을 출력하면 된다.
'''

N = int(input())
command = []
result = ''

for _ in range(N):
    command.append(input())
if len(command) == 1:
    print(command[0])
    exit()
    
for i in range(len(command[0])):
    sign = True
    for j in range(1,N):
        if command[j][i] != command[j-1][i]:
            sign = False
            continue
    if sign == True:
        result += command[j][i]
    elif sign == False:
        result += '?'

print(result)