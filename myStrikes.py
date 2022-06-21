import pygame
import myConstants


class Strike(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 2))
        self.image.fill(myConstants.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = vx
        self.speedy = vy

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

def breakout(x, y, x1, y1):
    if (x1 + 10 >= x >= x1) and (y1 + 10 >= y >= y1):
        return True
    return False
