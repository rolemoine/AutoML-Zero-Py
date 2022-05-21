from dataclasses import dataclass
from instruction import Instruction


@dataclass
class AlgorithmAbstract:
    setup_: list[Instruction]
    predict_: list[Instruction]
    learn_: list[Instruction]
