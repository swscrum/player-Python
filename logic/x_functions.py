from strategy import *
from models.base_level import BaseLevel


def base_overflow(base: Base):
    if base.population > gamestate.config.base_levels[base.level].max_population:
        print("base: overflow")
        return 1 # population is too high, people are dying, overflow
    elif base.population == gamestate.config.base_levels[base.level].max_population:
        print("base: max")
        return 0 # population is at it's limit spend now
    else:
        print("base: good")
        return -1 # population is fine, underflow


if __name__ == '__main__':
    print('hello world')
