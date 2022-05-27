from dataclasses import dataclass
from random import random
from typing import NoReturn
from algorithm import Algorithm
from instruction import Instruction
from enum import Op
import numpy as np
from random_generator import RandomGenerator


@dataclass
class Randomizer:
    allowed_setup_ops_: list[Op]
    allowed_predict_ops_: list[Op]
    allowed_learn_ops_: list[Op]
    bit_gen_: np.random.MT19937
    rand_gen_: RandomGenerator

    def __init__(
        self,
        allowed_setup_ops: list[Op],
        allowed_predict_ops: list[Op],
        allowed_learn_ops: list[Op],
        bit_gen: np.random.MT19937,
        rand_gen: RandomGenerator
    ) -> None:
        self.allowed_setup_ops_ = allowed_setup_ops
        self.allowed_predict_ops_ = allowed_predict_ops
        self.allowed_learn_ops_ = allowed_learn_ops
        self.bit_gen_ = bit_gen
        self.rand_gen_ = rand_gen

    @classmethod
    def randomize(cls, algorithm: Algorithm) -> NoReturn:
        if (cls.allowed_setup_ops_.empty()):
            cls.RandomizeSetup(algorithm)
        if (cls.allowed_predict_ops_.empty()):
            cls.RandomizePredict(algorithm)
        if (cls.allowed_learn_ops_.empty()):
            cls.RandomizePredict(algorithm)

    @classmethod
    def randomizeSetup(cls, algorithm: Algorithm) -> NoReturn:
        for instruction_index in range(len(algorithm.setup_)):
            instruction: Instruction = Instruction()
            instruction.setWithOp(cls.setupOp(), cls.rand_gen_)
            algorithm.setup_[instruction_index] = instruction

    @classmethod
    def RandomizePredict(cls, algorithm: Algorithm) -> NoReturn:
        for instruction_index in range(len(algorithm.predict_)):
            instruction: Instruction = Instruction()
            instruction.setWithOp(cls.predictOp(), cls.rand_gen_)
            algorithm.predict_[instruction_index] = instruction

    @classmethod
    def RandomizeLearn(cls, algorithm: Algorithm) -> NoReturn:
        for instruction_index in range(len(algorithm.learn_)):
            instruction: Instruction = Instruction()
            instruction.setWithOp(cls.learnOp(), cls.rand_gen_)
            algorithm.learn_[instruction_index] = instruction

    @classmethod
    def setupOp(cls) -> Op:
        return cls.allowed_setup_ops_[
            random.uniform(0, len(cls.allowed_setup_ops_))
        ]

    @classmethod
    def predictOp(cls) -> Op:
        return cls.allowed_predict_ops_[
            random.uniform(0, len(cls.allowed_predict_ops_))
        ]

    @classmethod
    def learnOp(cls) -> Op:
        return cls.allowed_learn_ops_[
            random.uniform(0, len(cls.allowed_learn_ops_))
        ]
