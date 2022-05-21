from dataclasses import dataclass
from typing import NoReturn, Type
from typing_extensions import Self
from algorithmAbstract import AlgorithmAbstract
from algorithmSerialize import AlgorithmSerialize
from instruction import Instruction


def isComponentFunctionEqual(
    componentFunction_1: list[Instruction],
    componentFunction_2: list[Instruction]
) -> bool:
    return componentFunction_1 == componentFunction_2


@dataclass
class Algorithm(AlgorithmAbstract):

    def __init__(self, algorithm: 'Algorithm' | AlgorithmSerialize) -> None:
        if (isinstance(algorithm, Algorithm)):
            self.setup_ = algorithm.setup_
            self.predict_ = algorithm.predict_
            self.learn_ = algorithm.learn_
        elif (isinstance(algorithm, AlgorithmSerialize)):
            self.fromProto(algorithm)

    @classmethod
    def opeatorEqual(self, algorithm: 'Algorithm') -> Type[Self@'Algorithm']:
        if (algorithm):
            self.setup_ = algorithm.setup_
            self.predict_ = algorithm.predict_
            self.learn_ = algorithm.learn_
        return self

    @classmethod
    def operatorEqualEqual(self, algorithm: 'Algorithm') -> bool:
        return (
            isComponentFunctionEqual(self.setup_, algorithm.setup_) and
            isComponentFunctionEqual(self.predict_, algorithm.predict_) and
            isComponentFunctionEqual(self.learn_, algorithm.learn_)
        )

    @classmethod
    def toReadable(self) -> str:
        instruction: Instruction
        print("def Setup():")
        for instruction in self.setup_:
            print(instruction.toReadable())
        print("def Predict():")
        for instruction in self.predict_:
            print(instruction.toReadable())
        print("def Learn():")
        for instruction in self.learn_:
            print(instruction.toReadable())

    @classmethod
    def toProto(self) -> AlgorithmSerialize:
        return AlgorithmSerialize(
            self.setup_.toProto(),
            self.predict_.toProto(),
            self.learn_.toProto()
        )

    @classmethod
    def fromProto(self, algorithmeSerialize: AlgorithmSerialize) -> NoReturn:
        self.setup_ = algorithmeSerialize.setup_.make_shared()
        self.predict_ = algorithmeSerialize.predict_.make_shared()
        self.learn_ = algorithmeSerialize.learn_.make_shared()
