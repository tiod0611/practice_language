array2D = []
for i in range(19):
    array2D.append(list(map(int, input().split(' '))))

n = int(input())
for _ in range(n):
    r, c = map(int, input().split(' '))
    r -= 1
    c -= 1
    for i in range(len(array2D)):
        if i == r: # 행이 같으면 반전
            for j in range(len(array2D[i])):
                array2D[i][j] = (array2D[i][j] - 1)**2

    for i in range(len(array2D)): # 행 변경
        for j in range(len(array2D[i])):
            if j == c:
                array2D[i][j] = (array2D[i][j] - 1)**2

for i in range(len(array2D)):
    for j in range(len(array2D[i])):
        print(array2D[i][j],end=' ')
    print()        