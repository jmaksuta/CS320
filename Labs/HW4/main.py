"""
Lab 04 - HW4
62.2 Lab 4: Longest Path
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""


def get_column(index, num_cols):
    """ Returns an index in column-space (n-space). """
    return index % num_cols


def get_row(index, num_cols):
    """ Returns an index in row-space (m-space). """
    return int(index / num_cols)


class Element:
    ''' Class representing the items of the trail table. '''
    def __init__(self, index=-1, value=0) -> None:
        """ Creates a new instance of Element. """
        self.index = index
        self.value = value


class ElementTrail:
    """ Defines a list of indexes and aggregate value. """
    def __init__(self, total=0, list=[]) -> None:
        """ Creates a new instance of ElementTrail. """
        self.total = total
        self.list = list

    def addElement(self, element=None) -> None:
        """ Appends the element to the end of the list and
        aggregates its value to the total. """
        self.total += element.value
        self.list.append(element.index)

    def get_last_element(self):
        """ Returns the last element of the list. """
        result = None
        length = len(self.list)
        if length > 0:
            result = self.list[length - 1]
        return result


def in_bounds(n_index, left, right):
    """ Checks if the index in column-space (n-space) is valid."""
    result = False
    if left < right:
        result = (n_index >= left and n_index <= right)
    else:
        result = (n_index >= left or n_index <= right)
    return result


def append_trails(lists, element, num_cols):
    """ Appends an element to a trail if it is valid. """
    result = []
    for a_list in lists:
        last_elem = a_list.get_last_element()
        # left column-space bound.
        l_bound = ((last_elem - 1) + num_cols) % num_cols
        # right column-space bound.
        r_bound = ((last_elem + 1) - num_cols) % num_cols
        # element index is column-space (n-space).
        n_index = get_column(element.index, num_cols)
        if in_bounds(n_index, l_bound, r_bound):
            # this index is within the bounds, its valid.
            new_group = ElementTrail(a_list.total, list(a_list.list))
            new_group.addElement(element)
            result.append(new_group)
    return result


def linear_index(row, col, num_cols):
    return (row * num_cols) + col


def make_trails(ribbon, trails, current_row, left_Bound, length):
    """ Returns valid trails for the column space indices in boundary. """
    result = []
    m = len(ribbon)
    n = len(ribbon[0])
    new_trails = trails
    # existing trails are the basis for new trails.
    for index in range(left_Bound, left_Bound + length):
        col = (index + n) % n
        row = current_row
        value = ribbon[row][col]
        l_index = linear_index(row, col, n)
        element = Element(l_index, value)
        new_trails = append_trails(trails, element, n)
        result += new_trails
    return result


def make_all_trails(ribbon):
    m = len(ribbon)
    n = len(ribbon[0])
    result = []
    # loops through the columns to find the plenko paths.
    for index in range(0, n):
        trails = []
        current_row = 0
        left_Bound = index
        right_bound = index
        while current_row < m:
            if current_row == 0:
                # add the index to the start of trail
                l_index = linear_index(current_row, index, n)
                value = ribbon[current_row][index]
                group = ElementTrail(value, [l_index])
                trails.append(group)
            else:
                # left bound in column space
                left_Bound = ((index - ((current_row - 1) + 1)) + n) % n
                # right bound in column space
                right_bound = ((index + ((current_row - 1) + 1)) - n) % n
                # length in linear space
                length = ((index + ((current_row - 1) + 1)) - (index - ((current_row - 1) + 1))) + 1
                # make trails for the column space indices in boundary.
                trails = make_trails(ribbon, trails, current_row, left_Bound, length)
            current_row += 1
        result += trails
    return result    


# Returns a group with the highest aggregate value.
def find_max_group(trail_groups):
    result = None
    max = 0
    for index in range(0, len(trail_groups)):
        group = trail_groups[index]
        if group.total > max:
            max = group.total
            result = group
    return result


# This is the internal function that calls main functions.
def internal_longest_path(ribbon):
    result = ()
    groups = make_all_trails(ribbon)
    max_group = find_max_group(groups)
    if max_group is not None:
        result = tuple(max_group.list)

    return result


# Validates the input argument
def validate(ribbon):
    # ribbon is not none
    assert (ribbon is not None)
    # row length is not zero
    assert (len(ribbon) > 0)
    # column length is not zero
    assert (len(ribbon[0]) > 0)
    return


def longest_path(ribbon):
    """ Returns the longest path of the ribbon. """
    result = ()
    try:
        validate(ribbon)
        result = internal_longest_path(ribbon)
        if len(result) < 2:
            result = ()

    except AssertionError as e:
        print(e)
        result = None
    return result
