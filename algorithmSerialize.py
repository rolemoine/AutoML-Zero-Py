from dataclasses import dataclass
from typing import Any
from algorithmAbstract import AlgorithmAbstract


@dataclass
class AlgorithmSerialize(AlgorithmAbstract):
    def __init__(self, setup: Any, predict:  Any, learn:  Any) -> None:
        self.setup_ = setup
        self.predict_ = predict
        self.learn_ = learn
