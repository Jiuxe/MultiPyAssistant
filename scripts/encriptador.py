import numpy as np
import random


def getGrillEncryptor():
    nxC,nyC = 25, 25

    gameState = np.zeros((nxC, nyC))

    n_neigh_good = 0
    n_neigh_bad = 0
    n_neigh_killer = 0

    # Generar moviles
    for num_mov in range(0,5):
        pivot = random.randint(2,nxC-2)
        gameState[pivot - 1,    pivot]      = 1
        gameState[pivot,        pivot + 1]  = 1
        gameState[pivot + 1,    pivot - 1]  = 1
        gameState[pivot + 1,    pivot]      = 1
        gameState[pivot + 1,    pivot + 1] = 1

    epocs = 200

    while epocs != 0:

        newGameState = np.copy(gameState)

        for y in range(0,nxC):
            for x in range(0,nyC):

                if gameState[x,y] == 3 or gameState[x,y] == 4:
                    n_neigh_good = 0
                    n_neigh_bad = 0
                    n_neigh_killer = 0
                    for i in range(-1,1):
                        for j in range(-1,1):
                            if not (i == 0 and j == 0):
                                if gameState[(x + i) % nxC, (y + j) % nyC] == 3:
                                    n_neigh_good += 1
                                elif gameState[(x + i) % nxC, (y + j) % nyC] == 4:
                                    n_neigh_bad += 1
                                elif gameState[(x + i) % nxC, (y + j) % nyC] == 6:
                                    n_neigh_killer += 1

                n_neigh = (gameState[(x - 1) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y - 1) % nyC]) % 2 + \
                          (gameState[(x - 1) % nxC, (y) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y) % nyC]) % 2 + \
                          (gameState[(x - 1) % nxC, (y + 1) % nyC]) % 2 + \
                          (gameState[(x) % nxC, (y + 1) % nyC]) % 2 + \
                          (gameState[(x + 1) % nxC, (y + 1) % nyC]) % 2

                # Regla 1 : Una celula muerta con 3 vecinas vivas, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla 2 : Una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

                # Regla 3: Una celula viva con 5 vecinos vivos, nace como una celula buena o mala
                if gameState[x, y] == 1 and n_neigh == 5:
                    newGameState[x, y] = random.choice([3, 4])

                # Regla 4: Una celula buena vecina de 2 o mas celulas malas, muere
                if gameState[x, y] == 3 and n_neigh_bad > 2:
                    newGameState[x, y] = 0

        gameState = np.copy(newGameState)

        epocs -= 1
    return gameState

grillEncryptor = getGrillEncryptor()
print(grillEncryptor)
