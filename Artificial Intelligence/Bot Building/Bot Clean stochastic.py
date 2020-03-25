#!/bin/python3

def nextMove(posr, posc, board):
    bot_pos = [posr, posc]
    dirty_pos = []
    flag = False
    for x in range(len(board)):
        if flag == True:
            break
        for y in range(len(board)):
            if board[x][y] == 'd':
                dirty_pos += [x, y]
                flag = True
        
    
    if bot_pos[1] < dirty_pos[1]:
        print("RIGHT")
    elif bot_pos[1] > dirty_pos[1]:
        print("LEFT")
    elif bot_pos[0] < dirty_pos[0]:
        print("DOWN")
    elif bot_pos[0] > dirty_pos[0]:
        print("UP")
    else:
        print("CLEAN")
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)