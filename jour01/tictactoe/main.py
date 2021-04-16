import pygame
from pygame.locals import *

from Init import *
from Interface import *




interface = Interface(480, 480, 60, 90)#(SCREEN_WIDTH, SCREEN_HEIGHT)

while True:
    pygame.display.update()
    DISPLAY.fill(BACKGROUND)
    interface.draw()
    FPS.tick(60)


    if ENDGAME > 1 and AI1 > 0:
        ENDGAME = interface.AI_move(1)
        DISPLAY.fill(BACKGROUND)
        interface.draw()
        cooldown = 500 - (pygame.time.get_ticks() - LAST_MOVE)
        time.delay(cooldown)
        LAST_MOVE = pygame.time.get_ticks()

    for event in pygame.event.get():
        if ENDGAME > 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    ENDGAME = interface.on_click(pygame.mouse.get_pos())
                    DISPLAY.fill(BACKGROUND)
                    interface.draw()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if ENDGAME > 1 and AI2 > 0:
        ENDGAME = interface.AI_move(-1)
        DISPLAY.fill(BACKGROUND)
        interface.draw()
        cooldown = 500 - (pygame.time.get_ticks() - LAST_MOVE)
        time.delay(cooldown)
        LAST_MOVE = pygame.time.get_ticks()

    if ENDGAME == 0:
        interface.reinitialize()
        ENDGAME = 2
    elif ENDGAME == 1 :
        interface.player_win(1)
        interface.reinitialize()
        ENDGAME = 2
        NEEDTOWAIT = True
    elif ENDGAME == -1:
        interface.player_win(-1)
        interface.reinitialize()
        ENDGAME = 2
        NEEDTOWAIT = True

"""   if NEEDTOWAIT:
        NEEDTOWAIT = False
        if AI1 == 0 or AI2 == 0:
            continue
        while (True):
            ev = pygame.event.wait()
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                break"""


def play():
