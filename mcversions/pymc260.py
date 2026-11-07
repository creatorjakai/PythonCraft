import pygame
import time
import sys
import os

def loadGAME():
    global running, screen, version, clock
    pygame.init()

    WINDOW_WIDTH = 1280
    WINDOW_HEIGTH = 720

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
    pygame.display.set_caption("PythonCraft 26")
    pygame.display.set_icon(icon)

    screen.fill((255, 83, 41))
    pygame.display.flip()

    running = True
    version = "v26.00c"
    clock = pygame.time.Clock()

    icon = pygame.image.load("assets/icons/icon.png")

    block_assets = {}
    item_assets = {}

    for filename in os.listdir("assets/blocks"):
        if filename.endswith(".png"):
            block_name = filename.removesuffix(".png")
            block_assets[block_name] = pygame.image.load(f"assets/blocks/{filename}").convert_alpha()

    for filename in os.listdir("assets/items"):
            if filename.endswith(".png"):
                item_name = filename.removesuffix(".png")
                item_assets[item_name] = pygame.image.load(f"assets/blocks/{filename}").convert_alpha()

loadGAME()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()