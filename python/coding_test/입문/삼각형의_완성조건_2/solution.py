'''
comment
삼각형이 이루는 조건은 2가지다.
삼각형의 변의 길이가 a, b, c이고 a가 가장 작은 변, b >= c 라고 할때

1. a + c > b
2. c <= b
이 두 조건을 만족하면 된다.

'''
def solution(sides):
    side_count = 0
    min_side = min(sides)
    max_side = max(sides)
    
    # 주어진 변 중 하나가 더 큰 경우
    for i in range(max_side):
        if (min_side + i) > max_side and i <= max_side:
            side_count += 1
    
    # 변하는 변의 길이가 더 큰 경우
    for i in range(max_side, min_side+max_side+1):
        if (min_side + max_side) > i and max_side <= i:
            side_count += 1

    return side_count

if __name__=="__main__":
    sides = [11, 7]
    result = solution(sides)
    print(result)