from dataclasses import dataclass
from tokenize import Double
from enum import HardcodedAlgorithmID
from algorithm import Algorithm
from computeCost import computeComponentFunctionCost
from generator import Generator


@dataclass
class TrainBudget:
    baseline_setup_cost_: Double
    baseline_train_cost_: Double
    threshold_factor_: Double

    def __init__(
        self,
        baseline_algorithm: Algorithm,
        threshold_factor: Double
    ) -> None:
        self.baseline_setup_cost_ = \
            computeComponentFunctionCost(baseline_algorithm.setup_)
        self.baseline_train_cost_ = \
            computeComponentFunctionCost(baseline_algorithm.predict_) + \
            computeComponentFunctionCost(baseline_algorithm.learn_)
        self.threshold_factor_ = threshold_factor

    @classmethod
    def trainExamples(cls, algorithm: Algorithm, budget: int) -> int:
        setup_cost: Double = computeComponentFunctionCost(algorithm.setup_)
        train_cost: Double = \
            computeComponentFunctionCost(algorithm.predict_) + \
            computeComponentFunctionCost(algorithm.learn_)
        assert train_cost > 0.0
        suggested_train_examples: Double = Double(budget)
        baseline_cost: Double = \
            cls.baseline_setup_cost_ + \
            (suggested_train_examples * cls.baseline_train_cost_)

        suggested_cost: Double = \
            setup_cost + suggested_train_examples * train_cost
        if suggested_cost <= baseline_cost * cls.threshold_factor_:
            return budget
        return 0


def buildTrainBudget(
    train_budget_spec: TrainBudgetSpec,
    generator: Generator
) -> TrainBudget:
    baseline_id: HardcodedAlgorithmID = \
        train_budget_spec.train_budget_baseline()
    baseline_algorithm: Algorithm = generator.modelByID(baseline_id)
    return TrainBudget(
        baseline_algorithm,
        train_budget_spec.train_budget_threshold_factor()
    )
