from enum import Op


def extractOps(ops_src: RepeatedField) -> list[Op]:
    return [ops_src.get(index) for index in range(len(ops_src))]
