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
        print(f"|{current_time}| - Killing process...")
        pygame.quit()
        sys.exit()

def updateLOADINGbar(progress, total):
    if progress == "reset" and total == "reset":
        for i in range(980):
            screen.fill((239, 50, 61))
            screen.blit(logo, (WINDOW_WIDTH // 2 - 250, WINDOW_HEIGHT // 2 - 225))
            pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 500, WINDOW_HEIGHT // 2 + 250, 1000, 50), 5)
            pygame.display.flip()
    elif progress == "reset" and total == "glide":
        for i in range(100):
            screen.fill((239, 50, 61))
            screen.blit(logo, (WINDOW_WIDTH // 2 - 250, WINDOW_HEIGHT // 2 - 225))
            updateLOADINGbar(100 - i, 100)
    else:
        length = (progress / total) * 980
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 500, WINDOW_HEIGHT // 2 + 250, 1000, 50), 5)
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 490, WINDOW_HEIGHT // 2 + 260, length, 30))
        pygame.display.flip()

def updateLOG(text):
    current_time = time.strftime("%H:%M:%S")
    print(f"|{current_time}| - {text}")

def loadGAME():
    global running, screen, version, clock, WINDOW_WIDTH, WINDOW_HEIGHT, logo, menu, framelimit
    pygame.init()
    updateLOG("Initialized library pygame")

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720

    running = True
    version = "v26.01b"
    clock = pygame.time.Clock()
    filesloaded = 0
    snapshot = False
    framelimit = 60

    if snapshot:
        icon = pygame.image.load("assets/icons/snapshot/icon.png")
    else:
        icon = pygame.image.load("assets/icons/icon.png")
    logo = pygame.transform.scale(pygame.image.load("assets/icons/logo/logo.png"), (500, 450))
    updateLOG("Loaded 2 files from assets/icons")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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

    time.sleep(0.1)
    menu = "mainmenu"
    return mainLOOP()

def mainLOOP():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if menu == "mainmenu":
            menuMAIN()
        else:
            running = False

        clock.tick(framelimit)

def menuMAIN():
    global menu
    a1 = pygame.transform.scale(pygame.image.load("assets/icons/titles/title.png"), (799, 207))
    a2 = pygame.transform.scale(pygame.image.load("assets/icons/titles/edition.png"), (400, 50))
    a3 = pygame.transform.scale(pygame.image.load("assets/icons/background.png"), (1280, 720))
    a4 = pygame.transform.scale(pygame.image.load("assets/textures/buttons/button.png"), (625, 62))
    a5 = pygame.transform.scale(pygame.image.load("assets/textures/buttons/button.png"), (625, 62))
    screen.blit(a3, (0, 0))
    screen.blit(a1, (WINDOW_WIDTH // 2 - 398, WINDOW_HEIGHT // 2 - 300))
    screen.blit(a2, (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 185))
    screen.blit(a4, (WINDOW_WIDTH // 2 - 312, WINDOW_HEIGHT // 2 - 50))
    screen.blit(a5, (WINDOW_WIDTH // 2 - 312, WINDOW_HEIGHT // 2 - 10))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a4.collidepoint(event.pos):
                menu = "singleplayer"
                return mainLOOP()
            if a5.collidepoint(event.pos):
                menu = "multiplayer"
                return mainLOOP()
    pygame.display.flip()

loadGAME()

pygame.quit()
sys.exit()