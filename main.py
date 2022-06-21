import random
import pygame
import myConstants
import myPlayer
import myStrikes
import time

# Default
pygame.init()
screen = pygame.display.set_mode((myConstants.WIDTH, myConstants.HEIGHT))
pygame.display.set_caption("Brawl Training")
clock = pygame.time.Clock()
screen.fill(myConstants.BLACK)
# Sprites
all_sprites = pygame.sprite.Group()
all_strikes = pygame.sprite.Group()

player = myPlayer.Player()
strike1 = myStrikes.Strike(0, 450, 3, 0)

all_sprites.add(player)
all_strikes.add(strike1)

all_sprites.draw(screen)
all_strikes.draw(screen)

f2 = pygame.font.SysFont('serif', 48)
text2 = f2.render("KRIEG", False,
                  (0, 180, 0))

# Цикл игры
running = True
now = start = time.time()
while running:
    if (time.time() - 1 > now):
        quantity = random.randint(3, 23) # количество ежесекундно добьавляющихся молний
        now = time.time()
        for i in range(quantity + 1):
            all_strikes.add(myStrikes.Strike(0, random.randint(0, myConstants.HEIGHT), 3 + 3 * random.random(), 0)) #
            all_strikes.add(myStrikes.Strike(random.randint(0, myConstants.WIDTH), 0, 0, 3 + 3 * random.random()))
            all_strikes.add(myStrikes.Strike(random.randint(0, myConstants.WIDTH), 0, 3 + 3 * random.random(), 3 + 3 * random.random()))
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
    for _ in all_strikes:
        if _.rect.x > myConstants.WIDTH or _.rect.y > myConstants.HEIGHT:
            all_strikes.remove(_)

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