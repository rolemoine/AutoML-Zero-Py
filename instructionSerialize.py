from dataclasses import dataclass
from instruction import Instruction
from instructionAbstract import InstructionAbstract


@dataclass
class InstructionSerialize(InstructionAbstract):

    def __init__(self, instruction: Instruction) -> None:
        self.op_ = instruction.op_
        # Must convert to higher precision (in1_, in2_, out_)
        self.in1_ = instruction.in1_
        self.in2_ = instruction.in2_
        self.out_ = instruction.out_
        self.activation_data = instruction.activation_data
        self.float_data_0_ = instruction.float_data_0_
        self.float_data_1_ = instruction.float_data_1_
        self.float_data_2_ = instruction.float_data_2_

    @classmethod
    def deserialize(self) -> Instruction:
        # TO FILL
        pass
