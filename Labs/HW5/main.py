"""
Lab 05 - HW5
63.2 Lab 5: Random Placement of Players
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

import random  # optional and you can delete this line if not useful

# subroutines if any, go here
# Green team starts on left half of square
left_side = []
# Gold team starts on right half of square
right_side = []

def get_length(field):
    return len(field)

def get_random(seed):
    return random.Random(seed)

def add_left(player):
    left_side.append(player)

def add_right(player):
    right_side.append(player)

def internal_placement(num_players, field):
    field_length = get_length(field)
    gen = get_random(100)
    side_length = int(field_length / 2)
    
    for index in range(0, field_length):
        continue

    pass

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
        internal_placement(num_players, field)
    except Exception as e:
        print(e)
    return result
