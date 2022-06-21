import pygame
import myConstants


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(myConstants.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (myConstants.WIDTH / 2, myConstants.HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > myConstants.WIDTH:
            self.rect.right = 0
        if self.rect.right > myConstants.HEIGHT:
            self.rect.left = 0
        dX, dY = pygame.mouse.get_pos()[0] - self.rect.x, pygame.mouse.get_pos()[1] - self.rect.y
        try:
            self.speedx = (myConstants.V ** 2) / (1 + abs(dY / dX)) * (dX / abs(dX))
        except ZeroDivisionError:
            self.speedx = 0
        try:
            self.speedy = (myConstants.V ** 2) / (1 + abs(dX / dY)) * (dY / abs(dY))
        except ZeroDivisionError:
            self.speedy = 0
