def solution(board, moves):
    basket = []
    cnt = 0

    for move in moves:
        move -= 1

        for i in range(len(board)):
            
            if board[i][move] == 0:
                continue

            basket.append(board[i][move])
            board[i][move] = 0
            break
        
        if len(basket) <= 1:
            continue
        
        while True:
            if len(basket) <= 1 or basket[-1] != basket[-2]:
                break
            basket = basket[:-2]
            cnt += 2

    return cnt


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
