import pygame
import numpy

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 135, 182, 189
ln = 255, 255, 25
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC   # Ancho de casilla
dimCH = height / nyC  # Alto de casilla

gameState = numpy.zeros((nxC, nyC))
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  for y in range(0, nxC):
    for x in range(0, nyC):
      posX = x * dimCW
      posY = y * dimCH

      poly = [(posX,         posY),
              (posX + dimCW, posY),
              (posX + dimCW, posY + dimCH),
              (posX,         posY + dimCH)]

      if gameState[x, y] == 1:
        pygame.draw.polygon(screen, ln, poly, 0)
      else:
        pygame.draw.polygon(screen, ln, poly, 1)

  pygame.display.flip()