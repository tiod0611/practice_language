'''
0 = not cute / 1 = cute
https://www.acmicpc.net/problem/10886

입력
첫 번째 줄에 설문조사를 한 사람의 수 N (1 ≤ N ≤ 101, N은 홀수)가 주어진다.

다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다. 0은 준희가 귀엽지 않다고 했다는 뜻이고, 1은 준희가 귀엽다고 했다는 뜻이다.

출력
준희가 귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고 귀엽다는 의견이 많을 경우 "Junhee is cute!"를 출력하라.
'''

N = int(input())
cute = not_cute = 0
for i in range(N):
    answer = input()
    if answer == '1':
        cute += 1
    elif answer == '0':
        not_cute += 1
result = '' if cute>not_cute else "not "
print(f"Junhee is {result}cute!")