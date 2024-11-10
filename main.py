import pygame
from platform import Platform
from ball import Ball
from enemy import Enemy
pygame.init()

scr_width = 1200
scr_height = 720
screen = pygame.display.set_mode((scr_width, scr_height))

platform = Platform((scr_width //2, scr_height - 100))
ball = Ball((platform.rect.centerx, platform.rect.centery - 50))

to_bonus = 5

enemies = list()
for x in range(50, screen.get_width() - 50, 50):
    for y in range(50, 151, 50):
        enemies.append(Enemy((x, y)))

clock = pygame.time.Clock()

running = True
while running:
    screen.fill('dark blue')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    platform.update(screen)
    ball.update(screen, platform)

    enemy = ball.check_hit(enemies)
    if enemy:
        enemies.remove(enemy)
        to_bonus -= 1
        if to_bonus == 0:
            ball.make_bigger()
            to_bonus = 5

    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.update()
    clock.tick(60)
