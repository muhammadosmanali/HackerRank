#

def nextMove(n,r,c,grid):
    bot_pos = [r, c]
    princes_pos = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == 'p':
                princes_pos += [x, y]
                

    if bot_pos[1] == princes_pos[1]:
        if bot_pos[0] > princes_pos[0]:
            return "UP"
        elif bot_pos[0] < princes_pos[0]:
            return "Down"
    
    if bot_pos[1] > princes_pos[1]:
        return "LEFT"
    elif bot_pos[1] < princes_pos[1]:
        return "RIGHT"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))