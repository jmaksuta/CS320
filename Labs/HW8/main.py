"""
Lab 08 - HW8
66.1 A Genetic Algorithm for the Traveling Salesperson Problem
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

import copy
from util import cost, valid_path, best_path

def get_cost(path, distances):
    result = 0
    for index in range(0, len(path)):
        a = path[index - 1]
        b = path[index]
        result += distances[(a,b)]
    return result


def generation(population, distances, gen):
    # best = None
    for index in range(1, len(population), 2):
        last = population[index - 1]
        # if best == None:
        #     best = last
        path = population[index]
        # last_cost = get_cost(last, distances)
        # path_cost = get_cost(path, distances)
        # is_valid = valid_path(path)
        # is_improved = (path_cost < last_cost)
        # if is_valid and is_improved:
        #     best = path
        # else:
        temp_path = list(copy.deepcopy(path))
        temp_last = list(copy.deepcopy(last))
        # step = 2 + (gen % 2)
        step = 1
        for place in range(0, len(path), step):            
            swap_a = temp_last[place]
            swap_b = temp_path[place]
            if swap_a != swap_b:
                i_last = temp_last.index(swap_b)
                i_path = temp_path.index(swap_a)
                temp_last = temp_last[:i_last] + temp_last[i_last + 1:]
                temp_path = temp_path[:i_path] + temp_path[i_path + 1:]
                temp_last = temp_last[:place] + [swap_b] + temp_last[place:]
                temp_path = temp_path[:place] + [swap_a] + temp_path[place:]

        temp_last = tuple(temp_last)
        temp_path = tuple(temp_path)
        
        if valid_path(temp_last) and cost(temp_last, distances) < cost(last, distances):
            population[index - 1] = temp_last

        if valid_path(temp_path) and cost(temp_path, distances) < cost(path, distances):
            population[index] = temp_path

    return (population, distances)


def _ga_tsp(initial_population, distances, generations) -> tuple:
    population = copy.deepcopy(initial_population)
    for gen in range(0, generations):
        population, distances = generation(population, distances, gen)

    result = best_path(initial_population, distances)
    best = best_path(population, distances)

    if cost(best, distances) < cost(result, distances):
        result = best

    return result


def validate(initial_population, distances, generations):
    """ Validates the input arguments, throws exception if
    there are invalid arguments."""
    assert initial_population is not None
    assert distances is not None
    assert generations is not None
     # if generations is not positive, ga_tsp should return None
    assert generations > 0
    return


def ga_tsp(initial_population, distances, generations) -> tuple:
    result = ()
    try:
        validate(initial_population, distances, generations)
        result = _ga_tsp(initial_population, distances, generations)

    except Exception as e:
        print(e)
        result = None
    return result
