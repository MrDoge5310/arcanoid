import pygame


class Enemy:
    def __init__(self, pos):
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 25))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self, scr):
        scr.blit(self.image, self.rect)

