"""
Lab 05 - HW5
63.2 Lab 5: Random Placement of Players
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

import random
import math


def get_length(field):
    """ Returns the length of field in one dimension. """
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


def free_spaces(field):
    """ Returns a list of two lists, left and right, and the
    linear indices of free spaces from field matrix. """
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

    return [left_field, right_field]


def package_result(lists):
    """ Packages the lists of two lists as tuple of two tuples. """
    return (tuple(lists[0]), tuple(lists[1]))


def place_player(flat_matrix, num_cols, index_to_place):
    """ Sets flat_matrix[index_to_place] = False and returns a
    tuple of the modified flat matrix, and the matrix coordinate
    at which the player was placed."""
    row = get_row(index_to_place, num_cols)
    col = get_column(index_to_place, num_cols)
    coordinate = (row, col)
    flat_matrix[index_to_place] = False
    return (flat_matrix, coordinate)


def place_player_in_field(flat_matrix, num_cols, side_field):
    """ Places a player a random selected index from side_field,
    removes the selected index from side_field, and returns a
    tuple of the modified flat_matrix, the modified side_field,
    and the placement matrix coordinate. """
    # choose a random index from the side
    choice_index = random.randint(0, len(side_field) - 1)
    field_index = side_field[choice_index]

    place_result = place_player(flat_matrix, num_cols, field_index)
    flat_matrix = place_result[0]
    coordinate = place_result[1]

    del side_field[choice_index]

    return (flat_matrix, side_field, coordinate)


def get_to_place_free_or_players(free_places, num_players):
    """ Compares free_places and num_players. If num_players is less
    than free_places, returns num_players, otherwise
    returns free_places. """
    result = free_places
    if num_players < free_places:
        result = num_players
    return result


def get_number_to_place(free, players_per_side):
    """ Returns the number of players to place. """
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
    """ Seeds random with random seed. """
    random.seed()


def internal_placement(num_players, field):
    """ This is the main internal process and returns a packaged result
    of coordinates on left and right sides of field. """
    result = [[], []]
    field_length = get_length(field)
    seed_random()
    players_per_side = num_players
    flat_matrix = flatten(field)
    
    if len(flat_matrix) > 0:
        free = free_spaces(field)
        number_to_place = get_number_to_place(free, players_per_side)
        # place player in pairs
        while number_to_place > 0:
            # place left
            left_result = place_player_in_field(flat_matrix, field_length, free[0])
            flat_matrix = left_result[0]
            free[0] = left_result[1]
            left_field_coordinate = left_result[2]
            result[0].append(left_field_coordinate)
            # place right
            right_result = place_player_in_field(flat_matrix, field_length, free[1])
            flat_matrix = right_result[0]
            free[1] = right_result[1]
            right_field_coordinate = right_result[2]
            result[1].append(right_field_coordinate)
            seed_random()
            
            number_to_place -= 1

    return package_result(result)


def validate(num_players, field):
    """ Validates the input argments. """
    assert field is not None
    assert type(field) is tuple
    assert type(field[0]) is tuple
    assert num_players is not None
    assert num_players > 0


# fill in placement
def placement(num_players, field):
    """ Returns a tuple of 2 tuples left and right that fills
    a field matix (m x m) with a random placement of num_players
    per side, left and right."""
    # default value
    result = ((), ()) 
    try:
        validate(num_players, field)
        result = internal_placement(num_players, field)

    except Exception as e:
        result = None
    return result
