from enum import Enum
from dataclasses import dataclass


@dataclass
class HardcodedAlgorithmID(Enum):
    NO_OP_ALGORITHM: int = 0
    RANDOM_ALGORITHM: int = 1
    LINEAR_ALGORITHM: int = 2
    NEURAL_NET_ALGORITHM: int = 3
    INTEGRATION_TEST_DAMAGED_NEURAL_NET_ALGORITHM: int = 4


@dataclass
class Op(Enum):
    NO_OP: int = 0    # OP0 in paper.
    SCALAR_SUM_OP: int = 1    # OP1 in paper.
    SCALAR_DIFF_OP: int = 2    # OP2 in paper.
    SCALAR_PRODUCT_OP: int = 3    # OP3 in paper.
    SCALAR_DIVISION_OP: int = 4    # OP4 in paper.
    SCALAR_ABS_OP: int = 5    # OP5 in paper.
    SCALAR_RECIPROCAL_OP: int = 6    # OP6 in paper.
    SCALAR_SIN_OP: int = 7    # OP7 in paper.
    SCALAR_COS_OP: int = 8    # OP8 in paper.
    SCALAR_TAN_OP: int = 9    # OP9 in paper.
    SCALAR_ARCSIN_OP: int = 10    # OP10 in paper.
    SCALAR_ARCCOS_OP: int = 11    # OP11 in paper.
    SCALAR_ARCTAN_OP: int = 12    # OP12 in paper.
    SCALAR_EXP_OP: int = 13    # OP13 in paper.
    SCALAR_LOG_OP: int = 14    # OP14 in paper.
    SCALAR_HEAVYSIDE_OP: int = 15    # OP15 in paper.
    VECTOR_HEAVYSIDE_OP: int = 16    # OP16 in paper.
    MATRIX_HEAVYSIDE_OP: int = 17    # OP17 in paper.
    SCALAR_VECTOR_PRODUCT_OP: int = 18    # OP18 in paper.
    SCALAR_BROADCAST_OP: int = 19    # OP19 in paper.
    VECTOR_RECIPROCAL_OP: int = 20    # OP20 in paper.
    VECTOR_NORM_OP: int = 21    # OP21 in paper.
    VECTOR_ABS_OP: int = 22    # OP22 in paper.
    VECTOR_SUM_OP: int = 23    # OP23 in paper.
    VECTOR_DIFF_OP: int = 24    # OP24 in paper.
    VECTOR_PRODUCT_OP: int = 25    # OP25 in paper.
    VECTOR_DIVISION_OP: int = 26    # OP26 in paper.
    VECTOR_INNER_PRODUCT_OP: int = 27    # OP27 in paper.
    VECTOR_OUTER_PRODUCT_OP: int = 28    # OP28 in paper.
    SCALAR_MATRIX_PRODUCT_OP: int = 29    # OP29 in paper.
    MATRIX_RECIPROCAL_OP: int = 30    # OP30 in paper.
    MATRIX_VECTOR_PRODUCT_OP: int = 31    # OP31 in paper.
    VECTOR_COLUMN_BROADCAST_OP: int = 32    # OP32 in paper.
    VECTOR_ROW_BROADCAST_OP: int = 33    # OP33 in paper.
    MATRIX_NORM_OP: int = 34    # OP34 in paper.
    MATRIX_COLUMN_NORM_OP: int = 35    # OP35 in paper.
    MATRIX_ROW_NORM_OP: int = 36    # OP36 in paper.
    MATRIX_TRANSPOSE_OP: int = 37    # OP37 in paper.
    MATRIX_ABS_OP: int = 38    # OP38 in paper.
    MATRIX_SUM_OP: int = 39    # OP39 in paper.
    MATRIX_DIFF_OP: int = 40    # OP40 in paper.
    MATRIX_PRODUCT_OP: int = 41    # OP41 in paper.
    MATRIX_DIVISION_OP: int = 42    # OP42 in paper.
    MATRIX_MATRIX_PRODUCT_OP: int = 43    # OP43 in paper.
    SCALAR_MIN_OP: int = 44    # OP44 in paper.
    VECTOR_MIN_OP: int = 45    # OP45 in paper.
    MATRIX_MIN_OP: int = 46    # OP46 in paper.
    SCALAR_MAX_OP: int = 47    # OP47 in paper.
    VECTOR_MAX_OP: int = 48    # OP48 in paper.
    MATRIX_MAX_OP: int = 49    # OP49 in paper.
    VECTOR_MEAN_OP: int = 50    # OP50 in paper.
    MATRIX_MEAN_OP: int = 51    # OP51 in paper.
    MATRIX_ROW_MEAN_OP: int = 52    # OP52 in paper.
    MATRIX_ROW_ST_DEV_OP: int = 53    # OP53 in paper.
    VECTOR_ST_DEV_OP: int = 54    # OP54 in paper.
    MATRIX_ST_DEV_OP: int = 55    # OP55 in paper.
    SCALAR_CONST_SET_OP: int = 56    # OP56 in paper.
    VECTOR_CONST_SET_OP: int = 57    # OP57 in paper.
    MATRIX_CONST_SET_OP: int = 58    # OP58 in paper.
    SCALAR_UNIFORM_SET_OP: int = 59    # OP59 in paper.
    VECTOR_UNIFORM_SET_OP: int = 60    # OP60 in paper.
    MATRIX_UNIFORM_SET_OP: int = 61    # OP61 in paper.
    SCALAR_GAUSSIAN_SET_OP: int = 62    # OP62 in paper.
    VECTOR_GAUSSIAN_SET_OP: int = 63    # OP63 in paper.
    MATRIX_GAUSSIAN_SET_OP: int = 64    # OP64 in paper.
