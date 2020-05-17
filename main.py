import pygame
import numpy
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 135, 182, 189
ln = 255, 255, 25
vc = 253, 145, 141
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC   # Ancho de casilla
dimCH = height / nyC  # Alto de casilla

gameState = numpy.zeros((nxC, nyC))
# Stick
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1
# Mover
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  newGameState = numpy.copy(gameState)
  for y in range(0, nxC):
    for x in range(0, nyC):
      ax = (x - 1) % nxC
      dx = (x + 1) % nxC
      ay = (y - 1) % nyC
      dy = (y + 1) % nyC
      nv = gameState[ax, ay] + \
          gameState[ax, y] + \
          gameState[ax, dy] + \
          gameState[x, ay] + \
          gameState[x, dy] + \
          gameState[dx, ay] + \
          gameState[dx, y] + \
          gameState[dx, dy]

      # Rule #1
      if gameState[x, y] == 0 and nv == 3:
        newGameState[x, y] = 1
      # Rule #2
      if gameState[x, y] == 1 and (nv < 2 or nv > 3):
        newGameState[x, y] = 0

      posX = x * dimCW
      posY = y * dimCH

      poly = [(posX,         posY),
              (posX + dimCW, posY),
              (posX + dimCW, posY + dimCH),
              (posX,         posY + dimCH)]

      if gameState[x, y] == 1:
        pygame.draw.polygon(screen, vc, poly, 0)
      else:
        pygame.draw.polygon(screen, bg, poly, 0)
      pygame.draw.polygon(screen, ln, poly, 2)

  gameState = newGameState
  pygame.display.flip()
  time.sleep(0.3)