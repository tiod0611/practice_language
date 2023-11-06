def solution(board, moves):
    basket = []
    answer = 0
    
    # moves에 따라 basket 체우기
    for m in moves:
        for i in range(board[0]):
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
            
        if len(basket) > 1 and basket[-1] == basket[-2]:
            answer += 2
            del basket[-2:]
        
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    result = solution(board, moves)
    print(result)