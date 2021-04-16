

def popInvalidePositions(possiblePositions, queen):
    invalids = []
    possiblePositions.remove(queen)
    for coord in possiblePositions:
        if coord[0] == queen[0]:
            invalids.append(coord)
            #possiblePositions.remove(coord)
            continue
        if coord[1] == queen[1]:
            invalids.append(coord)
            #possiblePositions.remove(coord)
            continue
        if (queen[0] - coord[0])**2 == (queen[1] - coord[1])**2:
            invalids.append(coord)
            #possiblePositions.remove(coord)
            continue
    for coord in invalids:
            possiblePositions.remove(coord)
    return invalids


def queens(solutions, possiblePositions, remainingQueens: int, queensPositions = []):
    if len(possiblePositions) == 0:
        return

    nextPossiblePositions = possiblePositions.copy()
    for position in possiblePositions:
        if remainingQueens == 1:
            queensPositions.append(position)
            solutions.append(queensPositions)
            return
        else:
            invalids = popInvalidePositions(nextPossiblePositions, position)
            nextQueensPositions = queensPositions.copy()
            nextQueensPositions.append(position)
            queens(solutions, nextPossiblePositions.copy(), remainingQueens - 1, nextQueensPositions)
            nextPossiblePositions += invalids
            invalids.clear()


boardSide = 8

squares = []
for i in range(0,boardSide):
    for j in range(0,boardSide):
        squares.append((i, j))

print(squares)

stop = False

solutions = []
queens(solutions, squares, boardSide)
print(len(solutions),"solutions found.")

for solution in solutions:
    for i in range(0, boardSide):
        line = ""
        for j in range(0, boardSide):
            if (i, j) not in solution:
                line += " O "
            else:
                line += " X "
        print(line)
    print()
    input("Press enter to continue")
    print()