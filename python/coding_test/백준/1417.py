'''
국회의원 선거
https://www.acmicpc.net/problem/1417

입력
첫째 줄에 후보의 수 N이 주어진다. 둘째 줄부터 차례대로 기호 1번을 찍으려고 하는 사람의 수, 기호 2번을 찍으려고 하는 수, 이렇게 총 N개의 줄에 걸쳐 입력이 들어온다. N은 50보다 작거나 같은 자연수이고, 득표수는 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 다솜이가 매수해야 하는 사람의 최솟값을 출력한다.
'''

N = int(input())
voters = []
count = 0
for _ in range(N):
    voters.append(int(input()))

while True:
    if voters.index(max(voters)) == 0:
        if voters.count(max(voters)) > 1:
            count += 1
        break
    voters[voters.index(max(voters))] -= 1
    voters[0] += 1
    count += 1

print(count)