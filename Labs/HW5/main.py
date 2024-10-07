"""
Lab 05 - HW5
63.2 Lab 5: Random Placement of Players
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

import random  # optional and you can delete this line if not useful
import math


def get_length(field):
    return len(field)


def get_column(index, num_cols):
    """ Returns a column coordinate given a linear index. """
    return index % num_cols


def get_row(index, num_cols):
    """ Returns a row coordinate given a linear index. """
    return int(index / num_cols)


def get_value(matrix, line_index, num_cols):
    """ returns the value of matrix at given linear index. """
    row = get_row(line_index, num_cols)
    col = get_column(line_index, num_cols)
    return matrix[row][col]


def linear_index(row, col, num_cols):
    """ Returns the linear index of (row,col) matrix coordinate. """
    return (row * num_cols) + col


def get_random(seed):
    return random.Random(seed)


def free_spaces(field):
    left_field = []
    right_field = []
    length = len(field)
    total_length = length * length
    mid = int(length / 2)
    for index in range(0, total_length):
        col = get_column(index, length)
        value = get_value(field, index, length)
        if col < mid and value is True:
            # left side
            left_field.append(index)
        elif col >= mid and value is True:
            # right side
            right_field.append(index)
    # shuffle the fields
    random.shuffle(left_field)
    random.shuffle(right_field)
    return [left_field, right_field]


def package_result(lists):
    return (tuple(lists[0]), tuple(lists[1]))


def place_player(flat_matrix, num_cols, index_to_place):
    row = get_row(index_to_place, num_cols)
    col = get_column(index_to_place, num_cols)
    coordinate = (row, col)
    flat_matrix[index_to_place] = False
    return (flat_matrix, coordinate)


def place_player_in_field(flat_matrix, num_cols, side_field, available):
    # choose a random index from the side
    choice_index = random.randint(0, len(side_field) - 1)
    field_index = side_field[choice_index]

    place_result = place_player(flat_matrix, num_cols, field_index)
    flat_matrix = place_result[0]
    coordinate = place_result[1]

    del side_field[choice_index]

    return (flat_matrix, side_field, field_index, coordinate)


def get_to_place_free_or_players(free_places, num_players):
    result = free_places
    if num_players < free_places:
        result = num_players
    return result


def get_number_to_place(free, players_per_side):
    left_free = len(free[0])
    right_free = len(free[1])
    left_num = get_to_place_free_or_players(left_free, players_per_side)
    right_num = get_to_place_free_or_players(right_free, players_per_side)
    return min(left_num, right_num)


def flatten(matrix):
    """ Flattens the ribbon matrix into a 1-dimensional list. """
    m = len(matrix)
    n = len(matrix[0])
    result = []
    try:
        for index in range(0, m * n):
            row = get_row(index, n)
            col = get_column(index, n)
            item = matrix[row][col]
            
            result.append(item)
            
    except Exception as ex:
        print(ex)
    return result


def seed_random():
    random.seed(random.randint(1, 1000))


def internal_placement(num_players, field):
    result = [[], []]
    field_length = get_length(field)
    seed_random()
    # side_length = int(field_length / 2)

    # remaining = int(num_players)

    players_per_side = num_players
    flat_matrix = flatten(field)
    
    free = free_spaces(field)
    left_free = len(free[0])
    right_free = len(free[1])
    number_to_place = get_number_to_place(free, players_per_side)
    while number_to_place > 0:
        # place player in pairs
        # place left
        left_result = place_player_in_field(flat_matrix, field_length, free[0], left_free)
        flat_matrix = left_result[0]
        free[0] = left_result[1]
        left_field_index = left_result[2]
        left_field_coordinate = left_result[3]
        result[0].append(left_field_coordinate)
        # place right
        right_result = place_player_in_field(flat_matrix, field_length, free[1], right_free)
        flat_matrix = right_result[0]
        free[1] = right_result[1]
        right_field_index = right_result[2]
        right_field_coordinate = right_result[3]
        result[1].append(right_field_coordinate)
        seed_random()
        
        number_to_place -= 1

    return package_result(result)


def validate(num_players, field):
    assert field is not None
    assert type(field) is tuple
    assert len(field) > 0
    assert type(field[0]) is tuple
    assert num_players is not None
    assert num_players > 0


# fill in placement
def placement(num_players, field):
    # default value
    result = ((), ()) 
    try:
        validate(num_players, field)
        result = internal_placement(num_players, field)

    except Exception as e:
        # print(e)
        result = ((), ())
    return result
