from typing import NoReturn
from taskInterface import TaskInterface


def defaultFirstParamSeeds():
    return {
        1001,  # Easy.
        1012,  # Medium(on easier side).
        1010,  # Medium(on harder side).
        1000,  # Hard.
        1006,  # Easy.
        1008,  # Medium(on easier side).
        1007,  # Medium(on harder side).
    }


def DefaultFirstDataSeeds():
    return {11001, 11012, 11010, 11000, 11006, 11008, 11007, 11003}


def fillTask(
    task_collection: TaskCollection,
    return_tasks: list[TaskInterface]
) -> NoReturn:
    # sourcery skip: simplify-len-comparison
    assert len(return_tasks) > 0
    for task in task_collection.tasks:
        FillTasksFromTaskSpec(task_spec, return_tasks)
