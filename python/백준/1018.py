'''
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''
array2D = [] # 체스판을 입력 받을 배열
mins = []

N, M = map(int, input().split(' '))

for _ in range(N):
    row = input()
    rowlist = [i for i in row]
    row = [1 if x == 'B' else -1 for x in row] # B => 1, W => -1
    array2D.append(row)

for r in range(N-7): # 아래로 8개씩, 1칸씩 이동
    for w in range(M-7): # 오른쪽으로 8개씩, 1칸씩 이동
        minimum = 0
        chess = array2D[r:r+8][w:w+8]
        
        for chessRow in chess:
            for i in range(0,8,2):
                if 0 != sum(chessRow[i:i+2]):
                    minimum += 1
                    print(minimum)
               
        mins.append(minimum)

print(min(mins))

'''
미완
test case 4번에서 카운팅이 잘 못되는 문제가 있음.
수정 예정
'''
