
import math

def find_nearest_dirty_pos(board, posx, posy, dimx, dimy):
    dirty_positions = []
    for x in range(dimx):
        for y in range(dimy):
            if board[x][y] == 'd':
                dirty_positions.append([x, y])
    
    nearest = []
    for dirty_pos in dirty_positions:
        eucli_dis = math.sqrt(((dirty_pos[0] - posx) ** 2) + ((dirty_pos[1] - posy) ** 2))
        nearest.append(eucli_dis)
    
    min_index = nearest.index(min(nearest))
    nearest_pos = dirty_positions[min_index]
    return nearest_pos


def next_move(posx, posy, dirty_pos):
    bot_pos = [posx, posy]
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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    dirty_pos = find_nearest_dirty_pos(board, pos[0], pos[1], dim[0], dim[1])
    next_move(pos[0], pos[1], dirty_pos)