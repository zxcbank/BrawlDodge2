import random
import pygame
import myConstants
import myPlayer
import myStrikes
import time
import other


# Default
pygame.init()
screen = pygame.display.set_mode((myConstants.WIDTH, myConstants.HEIGHT))
pygame.display.set_caption("Brawl Training")
clock = pygame.time.Clock()
screen.fill(myConstants.BLACK)
# Sprites Groups
all_sprites = pygame.sprite.Group()
all_strikes = pygame.sprite.Group()

player = myPlayer.Player()

all_sprites.add(player)

all_sprites.draw(screen)

# Цикл игры
running = True
now = start = time.time()
while running:
    if time.time() - 1 > now:
        quantity = random.randint(13, 23) # количество ежесекундно добьавляющихся молний
        now = time.time()
        for i in range(quantity + 1):
            other.generator(all_strikes)
    # Держим цикл на правильной скорости
    clock.tick(myConstants.FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Обновление
    all_sprites.update()
    all_strikes.update()

    # Рендеринг
    screen.fill(myConstants.BLACK)
    all_sprites.draw(screen)
    all_strikes.draw(screen)

    # исчезание молний
    other.StrikeDeath(all_strikes)

    # стокновения
    for _ in all_strikes:
        if myStrikes.breakout(_.rect.x, _.rect.y, player.rect.x, player.rect.y):
            all_sprites.remove(player)
            all_strikes.remove(all)
            running = False
            print(now - start, 'seconds')
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()