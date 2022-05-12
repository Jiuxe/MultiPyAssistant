import pygame
import numpy as np
import  time
import random

pygame.init()

width, height = 1000, 1000

screen = pygame.display.set_mode((height, width))

bg = 25,25,25
screen.fill(bg)

nxC,nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

def init_lg(epocs, direction=0, init_state=[]):

    if direction == 0:
        gameState = np.zeros((nxC, nyC))
        limit_down_x = 0
        limit_up_x = nxC
        limit_down_y = 0
        limit_up_y = nyC
        jump = 1
    else:
        gameState = init_state
        limit_down_x = nxC-1
        limit_up_x = 0
        limit_down_y = nyC-1
        limit_up_y = 0
        jump = -1

    # Generar moviles
    for num_mov in range(0,40):
        pivot = random.randint(2,48)
        gameState[pivot - 1,    pivot]      = 1
        gameState[pivot,        pivot + 1]  = 1
        gameState[pivot + 1,    pivot - 1]  = 1
        gameState[pivot + 1,    pivot]      = 1
        gameState[pivot + 1,    pivot + 1] = 1

    while epocs > 0:

        epocs -= 1
        newGameState = np.copy(gameState)

        screen.fill(bg)
        time.sleep(0.1)

        for y in range(limit_down_x,limit_up_x,jump):
            for x in range(limit_down_y,limit_up_y,jump):


                n_neigh = (gameState[(x - 1) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x - 1) % nxC, (y) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y) % nyC]) % 2 + \
                          (gameState[(x - 1) % nxC, (y + 1) % nyC]) % 2 + \
                          (gameState[(x) % nxC, (y + 1) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y + 1) % nyC]) % 2

                if direction == 0:
                    # Regla 1 : Una celula muerta con 3 vecinas vivas, "revive"
                    if gameState[x, y] == 0 and n_neigh == 3:
                        newGameState[x, y] = 1

                    # Regla 2 : Una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
                    elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                        newGameState[x, y] = 0
                else:
                    if not (gameState[x, y] == 0 and n_neigh == 3):
                        newGameState[x, y] = 0

                    elif not (gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3)):
                        newGameState[x, y] = 1


                poly = [((x) * dimCW, y * dimCH),
                       ((x+1) * dimCW, y * dimCH),
                       ((x+1) * dimCW, (y+1) * dimCH),
                       ((x) * dimCW, (y+1) * dimCH)]

                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen,(128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen,(255, 255, 255), poly, 0)

        gameState = np.copy(newGameState)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
    return gameState

gameState = init_lg(100)
gameState = init_lg(100, 1, gameState)