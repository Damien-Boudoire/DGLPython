import pygame

pygame.init()

FPS = pygame.time.Clock()

BACKGROUND = (50, 50, 50)
INTERFACE = (200, 200, 200)
X_TOKEN = (150, 225, 85)
O_TOKEN = (225, 100, 50)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

ENDGAME = 3

AI1 = 1
AI1_PLAYED = False
AI2 = 1
AI2_PLAYED = False

NEEDTOWAIT = False

LAST_CLIC = (-1, -1)

NEXT_PLAYER = 1

LAST_MOVE = pygame.time.get_ticks()

FONT = font_obj = pygame.font.Font('freesansbold.ttf', 32)

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY.fill(BACKGROUND)
pygame.display.set_caption("TicTacToe1337")
