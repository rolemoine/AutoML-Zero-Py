from dataclasses import dataclass
import logging
from tokenize import Double
from typing import Any
from algorithm import Algorithm


@dataclass
class Evaluator:
    fitness_combination_mode_: Any
    task_collection_: Any
    rand_gen_: Any
    functionnal_cache_: Any
    functinnal_cache_bit_gen_owned_: Any
    functional_cache_rand_gen_owned_: Any
    functional_cache_rand_gen_: Any
    best_fitness_: float
    max_abs_error_: Double
    num_train_steps_completed_: int
    tasks_: list[Any]
    fitness_combination_mode_: Any

    def __init__(self, **dictArgs: dict[str, Any]) -> None:
        if (dictArgs['Algorithm']):
            self.constructorFromAlgorithm(dictArgs['Algorithm'])
        else:
            self.constructorFromParam(dictArgs)

    @classmethod
    def constructorFromAlgorithm(cls, algorithm: Algorithm):
        task_fitnesses: list[Any] = []
        task_indexes: list[int] = list(range(len(cls.tasks_)))
        for task_index in task_indexes:
            task = cls.tasks_[task_index]
            assert task.MaxTrainExamples() >= kMinNumTrainExamples
            num_train_examples: int = None
            if cls.train_budget_ is None:
                num_train_examples = task.maxTrainExamples()
            else:
                num_train_examples = cls.train_budget_.TrainExamples(algorithm, task.MaxTrainExamples())

            curr_fitness: Double = -1.0
            curr_fitness = Execute(task, num_train_examples, algorithm)
            task_fitnesses.append(curr_fitness)
        combined_fitness: Double = CombineFitness(task_fitnesses, cls.fitness_combination_mode_)

        assert combined_fitness >= kMinFitness
        assert combined_fitness <= kMaxFitness

        return combined_fitness

    @classmethod
    def constructorFromParam(cls, **dictArgs: dict[str, Any | Double]):
        cls.fitness_combination_mode_ = dictArgs['fitness_combination_mode']
        cls.task_collection_ = dictArgs['task_collection']
        cls.train_budget_ = dictArgs['train_budget']
        cls.rand_gen_ = dictArgs['rand_gen']
        cls.functional_cache_ = dictArgs['functional_cache']
        cls.functional_cache_bit_gen_owned_ = {}
        cls.functional_cache_rand_gen_owned_ = {}
        cls.functional_cache_rand_gen_ = {}
        cls.best_fitness_ = -1.0
        cls.max_abs_error_ = dictArgs['max_abs_error']
        cls.num_train_steps_completed_ = 0
        fillTask()
        assert cls.tasks_.size() > 0

    @classmethod
    def execute(
        cls,
        task,
        num_train_examples,
        algorithm
    ) -> Double:
        match task.featuresSize():
            case 2:
                pass
            case 4:
                pass
            case 8:
                pass
            case 16:
                pass
            case 32:
                pass
            case _:
                logging.error("Unsupported features size.")

    @classmethod
    def getNumTrainStepsCompleted(cls) -> int:
        return cls.num_train_steps_completed_

    @classmethod
    def executeImpl(cls, task, num_train_examples, algorithm) -> Double:
        if cls.functional_cache_ is None:
            executor: Executor = Executor(
                algorithm,
                task,
                num_train_examples,
                task.validSteps(),
                cls.rand_gen_,
                cls.max_abs_error_)

            fitness: Double = executor.execute()
            cls.num_train_steps_completed_ += executor.getNumTrainStepsCompleted()
            return fitness
