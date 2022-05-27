from dataclasses import dataclass
from typing import Any
from op import Op


@dataclass
class InstructionAbstract:
    op_: Op
    # AddressT type
    in1_: Any
    in2_: Any
    out_: Any
    activation_data: float
    float_data_0_: float
    float_data_1_: float
    float_data_2_: float
