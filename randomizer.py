from dataclasses import dataclass
from random import random
from typing import Any, NoReturn
from algorithm import Algorithm
from instruction import Instruction
import numpy as np


@dataclass
class Randomizer:
    allowed_setup_ops_: list[Any]
    allowed_predict_ops_: list[Any]
    allowed_learn_ops_: list[Any]
    bit_gen_: np.random.MT19937
    rand_gen_: Any

    def __init__(
        self,
        allowed_setup_ops,
        allowed_predict_ops,
        allowed_learn_ops,
        bit_gen: np.random.MT19937,
        rand_gen
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
    def setupOp(cls) -> Any:
        return cls.allowed_setup_ops_[
            random.uniform(0, len(cls.allowed_setup_ops_))
        ]

    @classmethod
    def predictOp(cls) -> Any:
        return cls.allowed_predict_ops_[
            random.uniform(0, len(cls.allowed_predict_ops_))
        ]

    @classmethod
    def learnOp(cls) -> Any:
        return cls.allowed_learn_ops_[
            random.uniform(0, len(cls.allowed_learn_ops_))
        ]
