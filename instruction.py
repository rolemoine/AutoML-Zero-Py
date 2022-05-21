from dataclasses import dataclass
from typing import Any, NoReturn
from instructionAbstract import InstructionAbstract
from instructionSerialize import InstructionSerialize


@dataclass
class Instruction(InstructionAbstract):

    def __init__(self, **dictArgs: dict[str, Any]) -> None:
        self.op_ = dictArgs['op_'] or NO_OP
        self.in1_ = dictArgs['in1_'] or 0
        self.in2_ = dictArgs['in2_'] or 0
        self.out_ = dictArgs['out_'] or 0
        self.activation_data = dictArgs['activation_data'] or 0.0
        self.float_data_0_ = dictArgs['float_data_0_'] or 0.0
        self.float_data_1_ = dictArgs['float_data_1_'] or 0.0
        self.float_data_2_ = dictArgs['float_data_2_'] or 0.0

    @classmethod
    def FillWithNoOp(self) -> NoReturn:
        self.op_ = NO_OP
        self.in1_ = 0
        self.in2_ = 0
        self.out_ = 0
        self.activation_data_ = 0.0
        self.float_data_0_ = 0.0
        self.float_data_1_ = 0.0
        self.float_data_2_ = 0.0

    @classmethod
    def SetOpAndRandomizeParams(self, op, randomGenerator) -> None:
        # TO FILL
        self.FillWithNoOp()
        return

    @classmethod
    def AlterParam(self, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def RandomizeIn1(self, randomGenerator: Any) -> None:
        # TO FILL
        return
    
    @classmethod
    def RandomizeIn2(self, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def RandomizeOut(self, randomGenerator) -> None:
        # TO FILL
        return

    @classmethod
    def RandomizeData(self, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def AlterData(self, randomGenerator: Any) -> None:
        # TO FILL
        return

    @classmethod
    def toReadable(self) -> str:
        match self.op_:
            case NO_OP:
                return "\tNoOp()"
            case SCALAR_SUM_OP:
                return "\ts{} = s{} + s{}".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_DIFF_OP:
                return "\ts{} = s{} - s{}".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_PRODUCT_OP:
                return "\ts{} = s{} * s{}".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_DIVISION_OP:
                return "\ts{} = s{} / s{}".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_MIN_OP:
                return "\ts{} = minimum(s{}, s{})".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_MAX_OP:
                return "\ts{} = maximum(s{}, s{})".format(
                    self.out_, self.in1_, self.in2_)
            case SCALAR_ABS_OP:
                return "\ts{} = abs(s{})".format(
                    self.out_, self.in1_)
            case SCALAR_HEAVYSIDE_OP:
                return "\ts{} = heaviside(s{}, 1.0)".format(
                    self.out_, self.in1_)
            case SCALAR_CONST_SET_OP:
                return "\ts{} = {}".format(
                    self.out_, self.activation_data)
            # CONTINUE TO SCALAR_SIN_OP

    @classmethod
    def serialize(self) -> InstructionSerialize:
        return InstructionSerialize(self)
