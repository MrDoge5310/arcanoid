import pygame


class Ball:
    def __init__(self, pos):
        self.color = 'light blue'
        self.rect = pygame.rect.Rect(0, 0, 35, 35)
        self.rect.center = pos
        self.dx = 2
        self.dy = -2
        self.max_size = 180
        self.speed_ball = 25

    def update(self, screen, platform):
        self.move(screen, platform)
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.rect.width * 0.5)
        pygame.draw.circle(screen, 'yellow', self.rect.center, self.rect.width * 0.25)

    def make_bigger(self):
        if self.rect.width < self.max_size:
            self.rect.width *= 2
            self.rect.height *= 2

    def move(self, screen, platform):
        x, y = self.rect.center
        x += self.dx
        y += self.dy
        self.rect.center = (x, y)
        if x - self.speed_ball < 0 or x + self.speed_ball > screen.get_width():
            self.dx *= -1
        if y - self.speed_ball < 0:
            self.dy *= -1

        if self.rect.colliderect(platform.rect):
            self.dy *= -1

    def check_hit(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if abs(self.rect.right - enemy.rect.left) < abs(self.rect.left - enemy.rect.right) or \
                        abs(self.rect.left - enemy.rect.right) < abs(self.rect.right - enemy.rect.left):
                    self.dx *= -1
                if abs(self.rect.top - enemy.rect.bottom) > abs(self.rect.bottom - enemy.rect.top) or \
                        abs(self.rect.bottom - enemy.rect.top) < abs(self.rect.top - enemy.rect.bottom):
                    self.dy *= -1
                return enemy
