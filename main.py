import pygame
from platform import Platform
from ball import Ball
from enemy import Enemy
from random import randint
pygame.init()

scr_width = 1200
scr_height = 720
screen = pygame.display.set_mode((scr_width, scr_height))

platform = Platform((scr_width // 2, scr_height - 100))
init_ball = Ball((platform.rect.centerx, platform.rect.centery - 50))

balls = [init_ball]

to_bonus = 5

enemies = list()
for x in range(50, screen.get_width() - 50, 50):
    for y in range(50, 151, 50):
        enemies.append(Enemy((x, y)))

clock = pygame.time.Clock()

def split_ball(balls):
    new_balls = []
    for ball in balls:
        new_ball = Ball(ball.rect.center)
        new_ball.dx = -ball.dx
        new_ball.dy = ball.dy
        new_balls.append(new_ball)
    balls.extend(new_balls)

running = True
while running:
    screen.fill('dark blue')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    platform.update(screen)

    for ball in balls:
        ball.update(screen, platform)

        enemy = ball.check_hit(enemies)
        if enemy:
            enemies.remove(enemy)
            to_bonus -= 1
            if to_bonus == 0:
                bonus_number = 5 #randint(1, 6)
                if bonus_number == 1:
                    ball.make_bigger()
                elif bonus_number == 2:
                    split_ball(balls)
                elif bonus_number == 3:
                    platform.step += 8
                elif bonus_number == 4:
                    if platform.width_pl > 50:
                        platform.width_pl -= 25
                        platform.resize()
                elif bonus_number == 5:
                    for ball in balls:
                        ball.speed_ball += 25
                elif bonus_number == 6:
                    print("Збільшення ворогів")
                to_bonus = 5

    for enemy in enemies:
        enemy.draw(screen)

    pygame.display.update()
    clock.tick(60)
