def solution(sides):
    side_count = 0
    min_side = min(sides)
    max_side = max(sides)
    
    # 주어진 변 중 하나가 더 큰 경우
    for i in range(max_side):
        if (min_side + i) > max_side and i <= max_side:
            side_count += 1
    
    for i in range(max_side, min_side+max_side+1):
        if (min_side + max_side) > i and max_side <= i:
            side_count += 1

    return side_count

if __name__=="__main__":
    sides = [11, 7]
    result = solution(sides)
    print(result)