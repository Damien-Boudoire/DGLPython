

class Grid:

    def __init__(self):
        self.tiles = [[0,0,0],[0,0,0],[0,0,0]]

    def next_move(self, i, j, player):
        if self.tiles[i][j] == 0:
            self.tiles[i][j] = player
            return 1
        return -1

    def advancement(self):
        states = []
        #add rows
        all_lines = list(self.tiles)

        #add columns
        for i in range(0, 3):
            all_lines.append([ self.tiles[0][i],
                           self.tiles[1][i],
                           self.tiles[2][i]])

        #add diagonals
        all_lines.append([self.tiles[0][0], self.tiles[1][1], self.tiles[2][2]])
        all_lines.append([self.tiles[0][2], self.tiles[1][1], self.tiles[2][0]])

        for line in all_lines:
            states.append(sum(line))

        return states

    def is_finished(self):
        states = self.advancement()
        if max(states) == 3:
            return 1
        if min(states) == -3:
            return -1
        full = True
        for i in range(0,3):
            for j in range(0,3):
                if self.tiles[i][j] == 0:
                    full = False
        if full:
            return 0
        return 2

    def get(self, i, j):
        return self.tiles[i][j]