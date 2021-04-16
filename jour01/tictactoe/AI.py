import random

def AI_easy(grid, player):
    available_moves = []
    for i in range(0,3):
        for j in range(0,3):
            if grid.get(i, j) == 0:
                available_moves.append((i,j))


    return available_moves[random.randint(0,len(available_moves)-1)]

def AI_hard(grid, player):
    return AI_easy(grid, player)