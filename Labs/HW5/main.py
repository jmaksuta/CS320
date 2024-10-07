"""
Lab 05 - HW5
63.2 Lab 5: Random Placement of Players
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

import random  # optional and you can delete this line if not useful
import math

# subroutines if any, go here
# Green team starts on left half of square
left_side = []
# Gold team starts on right half of square
right_side = []

class Node:
    ''' A node in the linked list. '''
    def __init__(self, value) -> None:
        self.previous = None
        self.value = value
        self.next = None

class LinkedList:
    ''' A linked list. '''
    def __init__(self) -> None:
        self.last = None
        self.first = None
        self.length = 0

    def first(self):
        return self.first
    
    def last(self):
        return self.last
    
    def length(self):
        return self.length

    def append(self, value):
        if self.first is None:
            node = Node(value)
            self.last = node
            self.first = node
            node.previous = node
            node.next = node
            self.length += 1
        else:
            node = self.insertAfter(self.last, value)
            if node is not None:
                self.length += 1
            
    def insertAfter(self, parent, value):
        node = Node(value)
        # node.value = value
        node.previous = parent
        node.next = parent.next
        parent.next.previous = node
        parent.next = node
        self.last = node
        return node
    
    def remove(self, node):
        temp = node.value
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = None
        node.next = None
        return temp
    
    def pop(self):
        value = None
        value = self.remove(self.last)
        if value is not None:
            self.length -= 1
    
    def print_all(self):
        output = ""
        current = self.first
        output += "{value}".format(value=current.value)
        current = current.next
        while current is not self.last.next:
            output += ",{value}".format(value=current.value)
            current = current.next
        print(output)



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

def add_left(player):
    left_side.append(player)

def add_right(player):
    right_side.append(player)


LEFT_SIDE = 1
RIGHT_SIDE = 2

def free_spaces(field):
    left_field = []
    right_field = []
    length = len(field)
    total_length = length * length
    mid = int(length / 2)
    for index in range(0, total_length):
        col = get_column(index, length)
        value = get_value(field, index, length)
        if col < mid and value == True:
            # left side
            left_field.append(index)
        elif col >= mid and value == True:
            # right side
            right_field.append(index)
    return [left_field, right_field]


def package_result(lists):
    return (tuple(lists[0]), tuple(lists[1]))


def place_player(flat_matrix, num_cols, index_to_place):
    # num_cols = len(field)
    row = get_row(index_to_place, num_cols)
    col = get_column(index_to_place, num_cols)
    coordinate = (row, col)
    # field[row][col] = False
    flat_matrix[index_to_place] = False
    return (flat_matrix, coordinate)


def place_player_in_field(flat_matrix, num_cols, side_field, available):
    # num_cols = len(field)
    # choose a random index from the side
    choice_index = random.randint(0, len(side_field) - 1)
    field_index = side_field[choice_index]

    place_result = place_player(flat_matrix, num_cols, field_index)
    # (flat_matrix, coordinate)
    flat_matrix = place_result[0]
    coordinate = place_result[1]

    del side_field[choice_index]
    # row = get_row(field_index, num_cols)
    # col = get_column(field_index, num_cols)
    # field[row][col] = False
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
    # left_min = min(left_free, players_per_side)
    # right_min = min(right_free, players_per_side)
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
    result = [[],[]]
    field_length = get_length(field)
    seed_random()
    # gen = get_random(100)
    side_length = int(field_length / 2)

    remaining = int(num_players)

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
        # (flat_matrix, side_field, field_index, coordinate)
        flat_matrix = left_result[0]
        free[0] = left_result[1]
        left_field_index = left_result[2]
        left_field_coordinate = left_result[3]
        result[0].append(left_field_coordinate)
        # place right
        right_result = place_player_in_field(flat_matrix, field_length, free[1], right_free)
        # (flat_matrix, side_field, field_index, coordinate)
        flat_matrix = right_result[0]
        free[1] = right_result[1]
        right_field_index = right_result[2]
        right_field_coordinate = right_result[3]
        result[1].append(right_field_coordinate)
        seed_random()
        
        number_to_place -= 1
    # for index in range(0, field_length):
    #     continue

    return package_result(result)

def validate(num_players, field):
    assert field is not None
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
        print(e)
    return result
