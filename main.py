import pygame

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 135, 182, 189
ln = 255, 255, 25
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC   # Ancho de casilla
dimCH = height / nyC  # Alto de casilla

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

      pygame.draw.polygon(screen, ln, poly, 1)

  pygame.display.flip()