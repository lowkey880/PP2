import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins & PNGs")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)

background_img = pygame.image.load("/Users/arsenijkansin/Documents/labpp2/lab8/t-1/set/road_back.png").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

player_img = pygame.image.load("/Users/arsenijkansin/Documents/labpp2/lab8/t-1/set/car.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (60, 80))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 80))

enemy_img = pygame.image.load("/Users/arsenijkansin/Documents/labpp2/lab8/t-1/set/enemy_car.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (60, 80))

coin_img = pygame.image.load("/Users/arsenijkansin/Documents/labpp2/lab8/t-1/set/coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

player_speed = 5
coin_score = 0
enemy_speed_increase = 0

enemies = []
for _ in range(3):
    x = random.randint(40, WIDTH - 100)
    y = random.randint(-600, -100)
    speed = random.randint(3, 6)
    rect = enemy_img.get_rect(topleft=(x, y))
    enemies.append({"rect": rect, "speed": speed})

coins = []
for _ in range(3):
    x = random.randint(40, WIDTH - 80)
    y = random.randint(-600, -100)
    rect = coin_img.get_rect(topleft=(x, y))
    coins.append(rect)

running = True
while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_rect.left > 0:
        player_rect.move_ip(-player_speed, 0)
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_rect.right < WIDTH:
        player_rect.move_ip(player_speed, 0)

    for enemy in enemies:
        enemy["rect"].y += enemy["speed"]
        if enemy["rect"].top > HEIGHT:
            enemy["rect"].x = random.randint(40, WIDTH - 100)
            enemy["rect"].y = random.randint(-600, -100)
            enemy["speed"] = random.randint(3, 6) + enemy_speed_increase

    for coin in coins:
        coin.y += 4
        if coin.top > HEIGHT:
            coin.topleft = (random.randint(40, WIDTH - 80), random.randint(-600, -100))

    for enemy in enemies:
        if player_rect.colliderect(enemy["rect"]):
            text = font.render("Game Over!", True, (200, 0, 0))
            screen.blit(text, (WIDTH // 2 - 60, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    for coin in coins:
        if player_rect.colliderect(coin):
            coin_score += 1
            coin.topleft = (random.randint(40, WIDTH - 80), random.randint(-600, -100))
            if coin_score % 3 == 0:
                enemy_speed_increase += 1

    screen.blit(player_img, player_rect)

    for enemy in enemies:
        screen.blit(enemy_img, enemy["rect"])

    for coin in coins:
        screen.blit(coin_img, coin)

    score_text = font.render(f"Coins: {coin_score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(60)
