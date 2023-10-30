'''
https://www.acmicpc.net/problem/2751

문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

N = int(input()) # N을 몇으로 할지 입력
num = []
for i in range(N): # N개의 숫자 입력 받기
    num.append(int(input()))
for i in sorted(list(set(num))): # 중복을 제거하고 정렬한 뒤 출력
    print(i)