"""
Lab 08 - HW8
66.1 A Genetic Algorithm for the Traveling Salesperson Problem
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

def _ga_tsp(initial_population, distances, generations):
    pass


def validate(initial_population, distances, generations):
    """ Validates the input arguments, throws exception if
    there are invalid arguments."""
    assert initial_population is not None
    assert distances is not None
    assert generations is not None
     # if generations is not positive, ga_tsp should return None
    assert generations >= 0
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
