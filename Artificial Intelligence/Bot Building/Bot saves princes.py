#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    bot_pos = []
    princes_pos = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == 'm':
                bot_pos += [x, y]
            if grid[x][y] == 'p':
                princes_pos += [x, y]
    
    for x in range(0, abs(bot_pos[0] - princes_pos[0])):
        if bot_pos[0] > princes_pos[0]:
            bot_pos[0] -= 1
            print("UP")
        elif bot_pos[0] < princes_pos[0]:
            bot_pos[0] += 1
            print("DOWN")
        
    
    for x in range(0, abs(bot_pos[1] - princes_pos[1])):
        if bot_pos[1] > princes_pos[1]:
            bot_pos[1] -= 1
            print("LEFT")
        elif bot_pos[1] < princes_pos[1]:
            bot_pos[1] += 1
            print("RIGHT")
        elif bot_pos[0] == princes_pos[0]:
            break

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)