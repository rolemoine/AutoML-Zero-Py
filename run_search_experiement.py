from typing import Any, NoReturn


def run(config: Any) -> NoReturn:
    assert config is not None
    generator: Generator = Generator(
        config.initial_population,
        config.setup_size_init,
        config.predict_size_init,
        config.learn_size_init,
        extractOps(config.setup_ops),
        extractOps(config.predict_ops),
        extractOps(config.learn_ops),
        bit_gen,
        rand_gen
    )
    train_budget: Any = None
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
        bit_gen,
        rand_gen
    )