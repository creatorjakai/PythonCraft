import pygame
import time
import sys

def loadGAME():
    global running, screen
    pygame.init()

    WINDOW_WIDTH = 1280
    WINDOW_HEIGTH = 720

    running = True
    version = "v26.00b"

    icon = pygame.image.load("assets/icons/icon.png")
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
    pygame.display.set_caption("PythonCraft 26")
    pygame.display.set_icon(icon)

loadGAME()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()
sys.exit()