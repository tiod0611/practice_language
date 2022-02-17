'''
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''
import numpy as np

array2D = [] # 체스판을 입력 받을 배열
mins = []

N, M = map(int, input().split(' '))

for _ in range(N):
    row = input()
    rowlist = [i for i in row]
    row = [1 if x == 'B' else -1 for x in row] # B => 1, W => -1
    array2D.append(row)

array2D = np.array(array2D)
for r in range(N-7): # 아래로 8개씩, 1칸씩 이동
    for c in range(M-7): # 오른쪽으로 8개씩, 1칸씩 이동
        minimum = 0
        chess = array2D[r:r+8, c:c+8] # => 이거 안됨
        
        # 짝수 줄의 원소를 한칸씩 이동. 맨뒤는 맨앞으로 자리한다
        print("----")
        print(chess)
        for i in range(0,8,2):
            temp = chess[i][-1]
            chess[i][1:] = chess[i][:-1]
            chess[i][0] = temp
        print(chess)
        arrayChess = np.array(chess)
        colSum = np.einsum('ij->j', arrayChess)
        print(colSum)
        mins.append(np.sum(abs(colSum)))

print(mins)
print(min(mins)//2)

'''
미완
+ try1 (02.16)
    test case 4번에서 카운팅이 잘 못되는 문제가 있음.
    
+ try2 (02.17)
    채스 배열이 모두 올바른지 검사하기 위해 대각선의 원소가 모두 같을 때만 올바른 체스판이고 다른 원소 하나당 수정해야할 원소라고 판단
    코드 미완성
    numpy 모듈 사용했으니 백준에선 허용하지 않음

'''
