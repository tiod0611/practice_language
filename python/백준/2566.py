'''
최댓값
https://www.acmicpc.net/problem/2566

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

'''

max_value = 0
r_idx = 0
c_idx = 0

for i in range(9):
    row = list(map(int, input().split(' ')))
    if max(row) > max_value:
        max_value = max(row)
        r_idx = i+1
        c_idx = row.index(max(row)) + 1
print(max_value)
print(r_idx, c_idx)

# 1차 시기 
#   2차원 배열을 만들어 한 행씩 검사하며 최댓값과 인덱스를 구함

# 2차 시기
#   2차원 배열을 만들지 않고 입력 받는 배열에서 즉시 최댓값을 구하여 해당 값과 인덱스만 따로 저장