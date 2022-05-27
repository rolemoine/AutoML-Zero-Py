from dataclasses import dataclass
from typing import Any, NoReturn
from instructionAbstract import InstructionAbstract
from instructionSerialize import InstructionSerialize
from enum import Op


@dataclass
class Instruction(InstructionAbstract):
    def __init__(self) -> None:
        self.FillWithNoOp

    @classmethod
    def FillWithNoOp(cls) -> NoReturn:
        cls.op_ = Op.NO_OP
        cls.in1_ = 0
        cls.in2_ = 0
        cls.out_ = 0
        cls.activation_data_ = 0.0
        cls.float_data_0_ = 0.0
        cls.float_data_1_ = 0.0
        cls.float_data_2_ = 0.0

    @classmethod
    def setWithDict(cls, **dictArgs: dict[str, Any]) -> NoReturn:
        # NEED REFACTOR
        if (dictArgs['op_']):
            cls.op_ = dictArgs['op_']
        if (dictArgs['in1_']):
            cls.in1_ = dictArgs['in1_']
        if (dictArgs['in2_']):
            cls.in2_ = dictArgs['in2_']
        if (dictArgs['out_']):
            cls.out_ = dictArgs['out_']
        if (dictArgs['activation_data']):
            cls.activation_data = dictArgs['activation_data']
        if (dictArgs['float_data_0_']):
            cls.float_data_0_ = dictArgs['float_data_0_']
        if (dictArgs['float_data_1_']):
            cls.float_data_0_ = dictArgs['float_data_1_']
        if (dictArgs['float_data_2_']):
            cls.float_data_0_ = dictArgs['float_data_2_']

    @classmethod
    def setWithOp(cls, op: Any, rand_gen: Any) -> None:
        cls.setOpAndRandomizeParams(op, rand_gen)

    @classmethod
    def setWithInstruction(
        cls,
        instruction: 'Instruction',
        rand_gen: Any
    ) -> NoReturn:
        cls = instruction
        cls.alterParam(rand_gen)

    @classmethod
    def setWithSerialize(
        cls,
        instructionSerialize: 'InstructionSerialize',
        rand_gen: Any
    ) -> NoReturn:
        cls.deserialize(instructionSerialize)

    @classmethod
    def setOpAndRandomizeParams(cls, op: Op, randomGenerator) -> None:
        # TO FILL
        cls.FillWithNoOp()
        return

    @classmethod
    def alterParam(cls, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def randomizeIn1(cls, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def randomizeIn2(cls, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def randomizeOut(cls, randomGenerator) -> None:
        # TO FILL
        return

    @classmethod
    def randomizeData(cls, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def alterData(cls, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def toReadable(cls) -> str:
        match cls.op_:
            case Op.NO_OP:
                return "\tNoOp()"
            case Op.SCALAR_SUM_OP:
                return "\ts{} = s{} + s{}".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_DIFF_OP:
                return "\ts{} = s{} - s{}".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_PRODUCT_OP:
                return "\ts{} = s{} * s{}".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_DIVISION_OP:
                return "\ts{} = s{} / s{}".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_MIN_OP:
                return "\ts{} = minimum(s{}, s{})".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_MAX_OP:
                return "\ts{} = maximum(s{}, s{})".format(
                    cls.out_, cls.in1_, cls.in2_)
            case Op.SCALAR_ABS_OP:
                return "\ts{} = abs(s{})".format(
                    cls.out_, cls.in1_)
            case Op.SCALAR_HEAVYSIDE_OP:
                return "\ts{} = heaviside(s{}, 1.0)".format(
                    cls.out_, cls.in1_)
            case Op.SCALAR_CONST_SET_OP:
                return "\ts{} = {}".format(
                    cls.out_, cls.activation_data)
            # CONTINUE TO SCALAR_SIN_OP

    @classmethod
    def serialize(cls) -> InstructionSerialize:
        return InstructionSerialize(cls)

    @classmethod
    def deserialize(
        cls,
        instructionSerialize: InstructionSerialize
    ) -> NoReturn:
        cls.op_ = instructionSerialize.op()
        # TO FILL
        pass
