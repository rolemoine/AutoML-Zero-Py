from dataclasses import dataclass
from typing import Any


@dataclass
class InstructionAbstract:
    # Op type
    op_: Any
    # AddressT type
    in1_: Any
    in2_: Any
    out_: Any
    activation_data: float
    float_data_0_: float
    float_data_1_: float
    float_data_2_: float
