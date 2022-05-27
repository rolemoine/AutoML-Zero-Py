from typing import Any, NoReturn
from experiment_util import extractOps
from generator import Generator
from random_generator import RandomGenerator, generateRandomSeed
from train_budget import buildTrainBudget


# Add flag handler

def run(config: Any) -> NoReturn:
    random_seed: int = getFlag(FLAG['random_seed'])
    if (random_seed == 0):
        random_seed = generateRandomSeed()
    rand_gen: RandomGenerator = RandomGenerator()
    print(f"Random seed = {str(random_seed)}\n")

    assert config is not None
    
    generator: Generator = Generator(
        config.initial_population,
        config.setup_size_init,
        config.predict_size_init,
        config.learn_size_init,
        extractOps(config.setup_ops),
        extractOps(config.predict_ops),
        extractOps(config.learn_ops),
        # bit_gen,
        rand_gen
    )
    train_budget: buildTrainBudget = None
    if (config.has_train_budget):
        train_budget = buildTrainBudget(config.train_budget(), generator)
    mutator: Mutator = Mutator(
        config.allowed_mutation_types,
        config.mutate_prob,
        extractOps(config.setup_ops),
        extractOps(config.predict_ops),
        extractOps(config.learn_ops),
        config.mutate_setup_size_min,
        config.mutate_setup_size_max,
        config.mutate_predict_size_min,
        config.mutate_predict_size_max,
        config.mutate_learn_size_min,
        config.mutate_learn_size_max,
        # bit_gen,
        rand_gen
    )