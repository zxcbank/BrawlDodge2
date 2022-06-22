import random
import myConstants
import myStrikes


def generator(all_strikes):
    all_strikes.add(myStrikes.Strike(0, random.randint(0, myConstants.HEIGHT), 3 + 3 * random.random(), 0))  #
    all_strikes.add(myStrikes.Strike(random.randint(0, myConstants.WIDTH), 0, 0, 3 + 3 * random.random()))
    all_strikes.add(myStrikes.Strike(random.randint(0, myConstants.WIDTH), 0, 3 + 3 * random.random(), 3 + 3 * random.random()))

def StrikeDeath(all_strikes):
    for _ in all_strikes:
        if _.rect.x > myConstants.WIDTH or _.rect.y > myConstants.HEIGHT:
            all_strikes.remove(_)