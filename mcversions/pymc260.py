import pygame
import time
import sys
import os

def error(value, text):
    if value == 0:
        current_time = time.strftime("%H:%M:%S")
        print(f"ERROR: |{current_time}| - {text}")
    elif value == 1:
        current_time = time.strftime("%H:%M:%S")
        print(f"ERROR: |{current_time}| - {text}")
        print("Killing process...")
        pygame.quit()
        sys.exit()
    

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

    running = True
    version = "v26.00f"
    clock = pygame.time.Clock()
    filesloaded = 0
    snapshot = False

    if snapshot:
        icon = pygame.image.load("assets/icons/snapshot/icon.png")
    else:
        icon = pygame.image.load("assets/icons/icon.png")
    logo = pygame.transform.scale(pygame.image.load("assets/icons/logo/logo.png"), (500, 450))
    updateLOG("Loaded 2 files from assets/icons")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
    pygame.display.set_caption("PythonCraft 26")
    pygame.display.set_icon(icon)

    updateLOADINGbar("reset", "reset")

    block_assets = {}
    item_assets = {}

    for filename in os.listdir("assets/textures/block"):
        if filename.endswith(".png"):
            block_name = filename.removesuffix(".png")
            block_assets[block_name] = pygame.image.load(f"assets/textures/block/{filename}").convert_alpha()
            filesloaded += 1
            updateLOADINGbar(filesloaded, 1300)
    
    updateLOG(f"Loaded {filesloaded} files from assets/textures/block")

    filesloaded = 0
    updateLOADINGbar("reset", "glide")

    for filename in os.listdir("assets/textures/items"):
        if filename.endswith(".png"):
            item_name = filename.removesuffix(".png")
            item_assets[item_name] = pygame.image.load(f"assets/textures/items/{filename}").convert_alpha()
            filesloaded += 1
            updateLOADINGbar(filesloaded, 831)
    
    updateLOG(f"Loaded {filesloaded} files from assets/items")

    time.sleep(0.5)

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