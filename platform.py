import pygame


class Platform:
    def __init__(self, pos):
        self.color = 'yellow'
        self.width_pl = 200
        self.rect = pygame.rect.Rect(0, 0, self.width_pl, 50)
        self.rect.center = pos
        self.step = 8

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0, 15)

    def move(self, screen):
        win_width, win_height = screen.get_size()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.step

        elif keys[pygame.K_RIGHT] and self.rect.right <= win_width:
            self.rect.x += self.step

    def update(self, screen):
        self.draw(screen)
        self.move(screen)

    def resize(self):
        self.rect.width = self.width_pl
        self.rect.centerx = self.rect.centerx