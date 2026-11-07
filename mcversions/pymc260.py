import pygame
import time
import sys
import os

def updateLOADINGbar(progress, total):
    if progress and total == "reset":
        for i in range(980):
            screen.fill((239, 50, 61))
            screen.blit(logo, (WINDOW_WIDTH / 2 - 250, WINDOW_HEIGTH / 2 - 225))
            pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 500, WINDOW_HEIGTH // 2 + 250, 1000, 50), 5)
            pygame.display.flip()
    elif progress == "reset" and total == "glide":
        for i in range(100):
            screen.fill((239, 50, 61))
            screen.blit(logo, (WINDOW_WIDTH / 2 - 250, WINDOW_HEIGTH / 2 - 225))
            updateLOADINGbar(100 - i, 100)
    else:
        length = (progress / total) * 980
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 500, WINDOW_HEIGTH // 2 + 250, 1000, 50), 5)
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 490, WINDOW_HEIGTH // 2 + 260, length, 30))
        pygame.display.flip()

def updateLOG(text):
    current_time = time.strftime("%H:%M:%S")
    print(f"|{current_time}| - {text}")

def loadGAME():
    global running, screen, version, clock, WINDOW_WIDTH, WINDOW_HEIGTH, logo
    pygame.init()
    updateLOG("Initialized library pygame")

    WINDOW_WIDTH = 1280
    WINDOW_HEIGTH = 720

    icon = pygame.image.load("assets/icons/icon.png")
    logo = pygame.transform.scale(pygame.image.load("assets/icons/mojanglogo.png"), (500, 450))
    updateLOG("Loaded 2 files from assets/icons")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
    pygame.display.set_caption("PythonCraft 26")
    pygame.display.set_icon(icon)

    updateLOADINGbar("reset", "reset")

    running = True
    version = "v26.00d"
    clock = pygame.time.Clock()
    filesloaded = 0

    block_assets = {}
    item_assets = {}

    for filename in os.listdir("assets/blocks"):
        if filename.endswith(".png"):
            block_name = filename.removesuffix(".png")
            block_assets[block_name] = pygame.image.load(f"assets/blocks/{filename}").convert_alpha()
            filesloaded += 1
            updateLOADINGbar(filesloaded, 1300)
    
    updateLOG(f"Loaded {filesloaded} files from assets/blocks")

    filesloaded = 0
    updateLOADINGbar("reset", "glide")

    for filename in os.listdir("assets/items"):
        if filename.endswith(".png"):
            item_name = filename.removesuffix(".png")
            item_assets[item_name] = pygame.image.load(f"assets/items/{filename}").convert_alpha()
            filesloaded += 1
            updateLOADINGbar(filesloaded, 831)
    
    updateLOG(f"Loaded {filesloaded} files from assets/items")

    time.sleep(1)

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