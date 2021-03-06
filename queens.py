#!/usr/bin/env python3
from algorithms.features.ga import Base
from algorithms.operator import crossover
from algorithms.operator import evaluation
from algorithms.operator import fitness
from algorithms.operator import initialization
from algorithms.operator import mutation
from algorithms.operator import selection
from algorithms.views import ViewQueens
from collections import Counter
from view import ViewPlots

import random
import pylab as plt

import datetime
import os
import pathlib
import pickle


class Queens(Base, ViewQueens, ViewPlots):

    """Docstring for K-Queens. """

    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)
        ViewQueens.__init__(self, *args, **kwargs)
        ViewPlots.__init__(self, *args, **kwargs)


def run_init(obj, MAX_ITERATIONS=100, MAX_CHECK_FITNESS=10000):

    obj.initialization
    # obj.show_chromosomes_fitness

    average = []
    average.append(obj.average)
    bests = []
    bests.extend(map(lambda b: b[1], obj.best()))

    for step in range(1, MAX_ITERATIONS):
        obj.selection
        obj.crossover
        obj.mutation
        obj.evaluation

        bests.extend(map(lambda b: b[1], obj.best()))
        average.append(obj.average)

        if obj._counter_fitness >= MAX_CHECK_FITNESS:
            break

    with open(
        f"./outputs/random_data_bests"
        f"_max_i_{MAX_ITERATIONS}"
        f"_max_cf_{MAX_CHECK_FITNESS}.dat",
        "a",
    ) as arq:

        for best in bests:
            arq.write(f"{best},")

        arq.write("\n")

    with open(
        f"./outputs/random_data_average"
        f"_max_i_{MAX_ITERATIONS}"
        f"_max_cf_{MAX_CHECK_FITNESS}.dat",
        "a",
    ) as arq:

        for av in average:
            arq.write(f"{av},")

        arq.write("\n")

    # obj.plot_average_bests(average, bests)
    # obj.show_chromosomes_fitness
    # obj.show_best_five_individuals
    # obj.plot_bests(bests)


def run(
    obj,
    MAX_ITERATIONS=100,
    MAX_CHECK_FITNESS=10000,
    name_file="stacked",
    name_paths=".",
):

    # obj.show_chromosomes_fitness

    average = []
    average.append(obj.average)
    bests = []
    bests.extend(map(lambda b: b[1], obj.best()))

    for step in range(1, MAX_ITERATIONS):
        obj.selection
        obj.crossover
        obj.mutation
        obj.evaluation

        bests.extend(map(lambda b: b[1], obj.best()))
        average.append(obj.average)

        # if (obj._counter_fitness >= MAX_CHECK_FITNESS):
        #     break

    script_dir = os.path.dirname(os.path.abspath(__file__))

    target_dir = os.path.join(script_dir, "outputs", os.path.join(*name_paths))

    pathlib.Path(os.path.join(target_dir, "bests")).mkdir(
        parents=True, exist_ok=True
    )
    pathlib.Path(os.path.join(target_dir, "average")).mkdir(
        parents=True, exist_ok=True
    )

    name_file = name_file + ".dat"

    with open(os.path.join(target_dir, "bests", name_file), "a") as arq:

        for best in bests:
            arq.write(f"{best},")

        arq.write("\n")

    with open(os.path.join(target_dir, "average", name_file), "a") as arq:

        for av in average:
            arq.write(f"{av},")

        arq.write("\n")

    # obj.plot_average_bests(average, bests)
    # obj.plot_bests(bests)
    obj.show_chromosomes_fitness
    obj.show_best_five_individuals


if __name__ == "__main__":
    K = 8

    # parameters = dict(
    #     alleles=[list(range(K)) for _ in range(K)],
    #     k=K,
    #     population=100,
    #     operator={
    #         "selection": selection.choice_pairs_in_batch,
    #         "crossover": crossover.one_point_mating,
    #         "mutation": mutation.n_gene,
    #         "fitness": fitness.n_queens,
    #         "initialization": initialization.choice_yourself,
    #         "evaluation": evaluation.elitism,
    #     },
    #     params={
    #         "initialization": {"choice": random.choice},
    #         "selection": {"batch": 5, "choice_individual": random.choice},
    #         "mutation": {
    #             "n_point": 4,
    #             "choice_gene": random.randint,
    #             "choice_individual": random.choice,
    #             "mutation_gene": random.choice,
    #         },
    #         "crossover": {"mating_point": 4},
    #     },
    # )

    parameters = dict(
        alleles=[list(range(K)) for _ in range(K)],
        k=K,
        population=100,
        operator={
            "selection": selection.choice_pairs_in_batch,
            "crossover": crossover.one_point_mating,
            "mutation": mutation.n_swap,
            "fitness": fitness.n_queens,
            "initialization": initialization.choice_yourself,
            "evaluation": evaluation.elitism,
        },
        params={
            "initialization": {"choice": random.choice},
            "selection": {"batch": 5, "choice_individual": random.choice},
            "mutation": {
                "n_point": 2,
                "choice_gene": random.randint,
                "choice_individual": random.choice,
            },
            "crossover": {"mating_point": 4},
        },
    )

    # parameters = dict(
    #     alleles=[list(range(K)) for _ in range(K)],
    #     k=K,
    #     population=100,
    #     operator={
    #         'selection': selection.elitism,
    #         'crossover': crossover.one_point_mating,
    #         'mutation': mutation.n_gene,
    #         'fitness': fitness.n_queens,
    #         'initialization': initialization.choice_yourself,
    #         'evaluation': evaluation.elitism
    #     },
    #     params={
    #         'initialization': {
    #             'choice': random.choice
    #         },
    #         'selection': {
    #             'n_best': 16,
    #         },
    #         'mutation': {
    #             'n_point': 2,
    #             'choice_gene': random.randint,
    #             'choice_individual': random.choice,
    #             'mutation_gene': random.choice,
    #         },
    #         'crossover': {
    #             'mating_point': 4,
    #         },
    #     }
    # )

    queens = Queens(**parameters)

    name_chromossomes = "chromosomes_0.pkl"

    if not os.path.exists(name_chromossomes):
        queens.initialization
        pickle.dump(queens.chromosomes[::], open(name_chromossomes, "wb"))
        chromosomes_base = pickle.load(open(name_chromossomes, "rb"))
    else:
        chromosomes_base = pickle.load(open(name_chromossomes, "rb"))

    MAX_ITERATIONS = 100
    MAX_CHECK_FITNESS = 10000
    MAX_SIMULATIONS = 30

    DATETIME = datetime.datetime.utcnow().isoformat()

    rtn = lambda items: "::".join(
        [f"{k}:{v if not callable(v) else v.__name__}" for k, v in items]
    )

    name_paths = [
        "k",
        f"{queens.k}",
        "population",
        f"{queens.population}",
        "max_iterations",
        f"{MAX_ITERATIONS}",
        "max_check_fitness",
        f"{MAX_CHECK_FITNESS}",
        "max_simulations",
        f"{MAX_SIMULATIONS}",
        "initialization",
        f'{queens.operator.get("initialization").__name__}',
        f'{rtn(queens.params.get("initialization", {}).items())}',
        "fitness",
        f'{queens.operator.get("fitness").__name__}',
        f'{rtn(queens.params.get("fitness", {}).items())}',
        "selection",
        f'{queens.operator.get("selection").__name__}',
        f'{rtn(queens.params.get("selection", {}).items())}',
        "crossover",
        f'{queens.operator.get("crossover").__name__}',
        f'{rtn(queens.params.get("crossover", {}).items())}',
        "mutation",
        f'{queens.operator.get("mutation").__name__}',
        f'{rtn(queens.params.get("mutation", {}).items())}',
        "evaluation",
        f'{queens.operator.get("evaluation").__name__}',
        f'{rtn(queens.params.get("evaluation", {}).items())}',
    ]

    name_file = f"date_run_{DATETIME}"

    memoization = {}

    for _ in range(MAX_SIMULATIONS):

        memoization.update(queens._memoize_fitness)

        queens._memoize_fitness.update(memoization)

        print(len(queens._memoize_fitness.keys()))

        queens = Queens(**parameters)
        chromosomes_base = pickle.load(open(name_chromossomes, "rb"))
        queens.chromosomes = chromosomes_base[::]

        run(queens, MAX_ITERATIONS, MAX_CHECK_FITNESS, name_file, name_paths)
