from dataclasses import dataclass
import sys
import numpy as np
from time import time_ns
from random import gauss


@dataclass
class RandomGenerator():
    bit_gen_owned_: np.random.MT19937
    bit_gen_: np.random.MT19937

    # def __init__(self, bit_generator: np.random.MT19937) -> None:
    #    self.bit_gen_ = bit_generator
    def __init__(self) -> None:
        pass

    @classmethod
    def gaussianFloat(cls, mean: float, stdev: float) -> float:
        return gauss(mean, stdev)

    @classmethod
    def uniformInteger(cls, low: int, high: int) -> int:
        assert low >= -sys.maxint - 1
        assert high <= sys.maxint
        return int(np.random.uniform(low, high))

    @classmethod
    def uniformRandomSeed(cls) -> int:
        return int(np.random.uniform(1, sys.maxint))

    @classmethod
    # same for uniformDouble and uniformProbability
    def uniformFloat(cls, low: float, high: float) -> float:
        return np.random.uniform(low, high)


def generateRandomSeed() -> int:
    seed: int = 0
    while (seed == 0):
        seed = time_ns() % sys.maxint
    return seed
