'''
https://www.acmicpc.net/problem/7576
토마토

[풀이]
1. 익은 토마토(1)의 위치를 찾는다. 
    만약 익은 토마토(1)가 없다면 -1 출력 및 종료
2. 상하좌우에 있는 안 익은 토마토를 익힌다. 
3. 0 이 없다면 반복문이 돈 횟수를 출력하고 종료
    진행이 안되는데 0이 남았다면 -1 출력 및 종료
4. 위 작업을 반복한다. 


'''

# 토마토 상자 입력
# m, n = map(int, input().split(' '))
# tomato_box = []

# for _ in range(n):
#     row = [tomato for tomato in map(int, input().split(' '))]
#     tomato_box.append(row)

# # 익은 최초 토마토 좌표 구하기
# coordinates = []
# for i in range(len(tomato_box)):
#     for j in range(len(tomato_box[i])):
#         if tomato_box[i][j] == 1:
#             coordinates.append([i, j])

# day = 0

# 익지 못하는 토마토를 제외하고 모든 토마토가 익었는지 어떻게 알 수 있을까? 
# while True:





## 정답 필사 ##
# 출처 chat-gpt
from collections import deque

# 입력 받기
m, n = map(int, input().split()) ## split()에 ' ' 스페이스를 입력하지 않아도 잘 처리되나 보다.
grid = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0] ## 행 변화량. -1은 왼쪽 방향, 1은 오른쪽 방향
dy = [0, 0, -1, 1] ## 열 변화량. -1은 위쪽 방향, 1은 아래쪽 방향
## 근데 왜 0, 0이 필요할까

## 넓이 우선 탐색으로 모든 토마토를 익힌다.
def bfs():
    queue = deque()

    # 익은 토마토의 위치를 큐에 넣기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0)) # 위치와 일수를 함께 저장
                print("queue.append(i, j, 0) : ", i, j, 0)
                ## 왜 일수를 저장할까? 토마토의 위치까지 도달하는 것과 일수가 의미가 있나?
    
    while queue:
        x, y, days = queue.popleft() ## deque는 양쪽에서 데이터를 꺼낼 수 있는 자료구조다. popleft()는 왼쪽에서 데이터를 꺼내는 메서드다.
        print("x, y, days : ", x, y, days)
        # 상하좌우 확인
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            ## 반복문이 4인 것은 상하좌우 방향으로 한번씩 살펴보기 위함이다.
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                ## 조건에 대해서 자세히 살펴보자.
                # 0 <= nx < n : 행 위치가 토마토 박스 안에 있어야 하고
                # 0 <= ny < m : 열 위치가 토마토 박스 안에 있어야 하고
                # grid[nx][ny] == 0 : 토마토가 안 익은 것이라면(당연히 빈 토마토 방지)
                grid[nx][ny] = 1 # 토마토 익히기
                queue.append((nx, ny, days + 1)) # 큐에 추가하기 ## days에 추가한다.
                print("queue.append(nx, ny, days + 1) : ", nx, ny, days+1)            
            
            else:
                print("nx, ny : ", nx, ny)

    # 모든 토마토가 익었는지 확인
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0: ## 안 익은 토마토가 있다면
                return -1 

    return days # 모든 토마토가 익은 경우 최소 일수 반환

# BFS 실행
result = bfs()

# 결과 출력
print(result)