import pygame
from pygame import *
from Init import *


class Tile:
    def __init__(self, row, column, x, y, width, height):
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, token):
        if token < 0:
            width = self.width * 0.9
            height = self.height * 0.9

            pygame.draw.line(DISPLAY, X_TOKEN, (self.rect.centerx - width / 2, self.rect.centery + height / 2),
                                               (self.rect.centerx + width / 2, self.rect.centery - height / 2), 10)
            pygame.draw.line(DISPLAY, X_TOKEN, (self.rect.centerx - width / 2, self.rect.centery - height / 2),
                                               (self.rect.centerx + width / 2, self.rect.centery + height / 2), 10)

        if token > 0:
            width = self.width * 0.9

            pygame.draw.circle(DISPLAY, O_TOKEN, (self.rect.centerx, self.rect.centery), width / 2)
            pygame.draw.circle(DISPLAY, BACKGROUND, (self.rect.centerx, self.rect.centery), width / 2 - 10)

    def collidepoint(self, coord):
        return self.rect.collidepoint(coord)