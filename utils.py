def matrixToString(matrix) -> str:
    res: str = "\n["
    for col in matrix:
        res += "["
        for line in col:
            res += f"{matrix[col, line]},"
        res += "],\n"
    return res + "],\n"
