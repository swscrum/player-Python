from models.base import Base
from models.base_level import BaseLevel


def base_overflow(base: Base):
    if base.population > BaseLevel(base.level).max_population:
        return 1  # population is too high, people are dying
    elif base.population == BaseLevel(base.level).max_population:
        return 0  # population is at it's limit spend now
    else:
        return -1  # population is fine


if __name__ == '__main__':
    print('hello world')
