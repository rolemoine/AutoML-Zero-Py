from dataclasses import dataclass
from enum import Op


@dataclass
class InstructionAbstract:
    op_: Op
    # AddressT type
    in1_: int
    in2_: int
    out_: int
    activation_data: float
    float_data_0_: float
    float_data_1_: float
    float_data_2_: float
