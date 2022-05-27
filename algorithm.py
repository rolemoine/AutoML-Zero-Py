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
    def opeatorEqual(cls, algorithm: 'Algorithm') -> Type[Self@'Algorithm']:
        if algorithm:
            cls.setup_ = algorithm.setup_
            cls.predict_ = algorithm.predict_
            cls.learn_ = algorithm.learn_
        return cls

    @classmethod
    def operatorEqualEqual(cls, algorithm: 'Algorithm') -> bool:
        return (
            isComponentFunctionEqual(cls.setup_, algorithm.setup_) and
            isComponentFunctionEqual(cls.predict_, algorithm.predict_) and
            isComponentFunctionEqual(cls.learn_, algorithm.learn_)
        )

    @classmethod
    def toReadable(cls) -> str:
        instruction: Instruction
        print("def Setup():")
        for instruction in cls.setup_:
            print(instruction.toReadable())
        print("def Predict():")
        for instruction in cls.predict_:
            print(instruction.toReadable())
        print("def Learn():")
        for instruction in cls.learn_:
            print(instruction.toReadable())

    @classmethod
    def toProto(cls) -> AlgorithmSerialize:
        return AlgorithmSerialize(
            cls.setup_.toProto(),
            cls.predict_.toProto(),
            cls.learn_.toProto()
        )

    @classmethod
    def fromProto(cls, algorithmeSerialize: AlgorithmSerialize) -> NoReturn:
        cls.setup_ = algorithmeSerialize.setup_.make_shared()
        cls.predict_ = algorithmeSerialize.predict_.make_shared()
        cls.learn_ = algorithmeSerialize.learn_.make_shared()
