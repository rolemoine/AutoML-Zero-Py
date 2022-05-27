from dataclasses import dataclass
from instruction import Instruction
from randomizer import Randomizer
import numpy as np
from random_generator import RandomGenerator
from enum import HardcodedAlgorithmID, Op


@dataclass
class Generator():
    init_model_: HardcodedAlgorithmID
    setup_size_init_: int
    predict_size_init_: int
    learn_size_init_: int
    allowed_setup_ops_: list[Op]
    allowed_predict_ops_: list[Op]
    allowed_learn_ops_: list[Op]
    bit_gen_owned_: np.random.mt19937
    rand_gen_owned_: RandomGenerator
    # rand_gen_: RandomGenerator
    randomizer_: Randomizer
    no_op_instruction_: Instruction

    def __init__(
        self,
        init_model: HardcodedAlgorithmID,
        setup_size_init: int,
        predict_size_init: int,
        learn_size_init: int,
        allowed_setup_ops: list[Op],
        allowed_predict_ops: list[Op],
        allowed_learn_ops: list[Op],
        bit_gen_owned: np.random.mt19937,
        rand_gen_owned: RandomGenerator,
        rand_gen: RandomGenerator,
        randomizer: Randomizer,
        no_op_instruction: Instruction
    ) -> None:
        self.init_model_ = init_model
        self.setup_size_init_ = setup_size_init
        self.predict_size_init_ = predict_size_init
        self.learn_size_init_ = learn_size_init
        self.allowed_setup_ops_ = allowed_setup_ops
        self.allowed_predict_ops_ = allowed_predict_ops
        self.allowed_learn_ops_ = allowed_learn_ops
        self.bit_gen_owned_ = bit_gen_owned
        self.rand_gen_owned_ = rand_gen_owned
        # self.rand_gen_ = rand_gen
        self.randomizer_ = randomizer
        self.no_op_instruction_ = no_op_instruction
