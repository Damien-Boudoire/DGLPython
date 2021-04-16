from Init import *
from Grid import *
from Tile import *

import AI

class Interface:
    def __init__(self, width, height, x = 0, y = 0):
        self.x = x
        self.y = y
        self.grid = Grid()
        self.tiles = []
        for i in range(0, 3):
            for j in range(0, 3):
                self.tiles.append(Tile(i, j, self.x + i * (width/3), self.y + j * (height/3), width/3, height/3))

        self.score = [0, 0]

        self.width = width
        self.height = height

        self.current_player = 1

        self.update_score_box()

    def reinitialize(self):
        self.grid = Grid()

    def update_score_box(self):
        score_O_surface = FONT.render(str(self.score[0]), True, O_TOKEN, BACKGROUND)
        score_X_surface = FONT.render(str(self.score[1]), True, X_TOKEN, BACKGROUND)

        score_O_rect = score_O_surface.get_rect()
        score_X_rect = score_X_surface.get_rect()

        score_O_rect.center = (SCREEN_WIDTH / 2 - 45, 40)
        score_X_rect.center = (SCREEN_WIDTH / 2 + 45, 40)

        self.scoreBox_O = (score_O_surface, score_O_rect)
        self.scoreBox_X = (score_X_surface, score_X_rect)

    def draw(self):
        #draw score
        DISPLAY.blit(self.scoreBox_O[0], self.scoreBox_O[1])
        pygame.draw.line(DISPLAY, INTERFACE, (SCREEN_WIDTH / 2, 15), (SCREEN_WIDTH / 2, 60), width=5)
        DISPLAY.blit(self.scoreBox_X[0], self.scoreBox_X[1])

        #draw lines
        pygame.draw.line(DISPLAY, INTERFACE, (self.x + 0, self.y + self.height / 3),
                                             (self.x + self.width, self.y + self.height / 3))
        pygame.draw.line(DISPLAY, INTERFACE, (self.x + 0, self.y + 2 * self.height / 3),
                                             (self.x + self.width, self.y + 2 * self.height / 3))

        pygame.draw.line(DISPLAY, INTERFACE, (self.x + self.width / 3, self.y + 0),
                                             (self.x + self.width / 3, self.y + self.height))
        pygame.draw.line(DISPLAY, INTERFACE, (self.x + 2 * self.width / 3, self.y + 0),
                                             (self.x + 2 * self.width / 3, self.y + self.height))

        #draw tiles
        for tile in self.tiles:
            tile.draw(self.grid.get(tile.row, tile.column))

    def player_win(self, player):
        if player > 0:
            self.score[0] += 1
        else:
            self.score[1] += 1
        self.update_score_box()

    def on_click(self, coord):
        for tile in self.tiles:
                if tile.collidepoint(coord):
                    if self.grid.next_move(tile.row, tile.column, self.current_player) > 0:
                        self.current_player = -1 if self.current_player == 1 else 1
        return self.grid.is_finished()

    def AI_move(self, player):
        move=(0,0)
        move_accepted = -1
        while move_accepted < 0:
            if player > 0:
                if AI1 == 1:
                    move = AI.AI_easy(self.grid, player)
                elif AI1 == 2:
                    move = AI.AI_hard(self.grid, player)
            elif player < 0:
                if AI2 == 1:
                    move = AI.AI_easy(self.grid, player)
                elif AI2 == 2:
                    move = AI.AI_hard(self.grid, player)
            move_accepted = self.grid.next_move(move[0], move[1], player)
        return self.grid.is_finished()