"""
Lab 04 - HW4
62.2 Lab 4: Longest Path
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""


import math


ROW_INDEX = 0
COL_INDEX = 1
VALUE_INDEX = 2


# -----------BEGIN HEAP SORT-------------------
def _swap(the_heap, up_elem_index, down_elem_index):
    """ swaps the elements in the list at indices up_elem_index
    and down_elem_index. """
    temp = the_heap[up_elem_index]
    the_heap[up_elem_index] = the_heap[down_elem_index]
    the_heap[down_elem_index] = temp
    return


def _greater_than(left_operand, right_operand):
    """ Returns True if left_operand is greater than right_operand. """
    return left_operand > right_operand


def insert(the_heap, element=None, ribbon=(())) -> None:
    """ Inserts an element into the heap and heapifys. """
    the_heap.append(element)
    last_index = len(the_heap) - 1
    current_index = last_index

    while current_index > 0 and _greater_than(
            the_heap[int((current_index - 1) / 2)][VALUE_INDEX],
            the_heap[current_index][VALUE_INDEX]):
        parent_index = int((current_index - 1) / 2)
        child_index = current_index
        _swap(the_heap, parent_index, child_index)
        current_index = parent_index
    return


def _index_of_smaller(the_heap, index_a, index_b):
    """ Compares element at index_a with element at index_b and
    returns the index of the smaller of the two."""
    result = -1
    if the_heap[index_a][VALUE_INDEX] <= the_heap[index_b][VALUE_INDEX]:
        result = index_a
    else:
        result = index_b
    return result


def _to_index(nth_value):
    """ Returns the index value an the nth value.
    i.e. the nth element has an index n - 1. """
    return nth_value - 1


def _nth_elem(the_heap, n):
    """ Returns the nth element. """
    return the_heap[_to_index(n)]


def remove_minimum_element(the_heap):
    """ Removes the minimum element from the heap, the first element,
    and heapifys"""
    temp = the_heap[0]
    length_of_list = len(the_heap)
    the_heap[0] = _nth_elem(the_heap, length_of_list)
    length_of_list = length_of_list - 1
    del the_heap[length_of_list]
    current_index = 0
    while current_index < length_of_list:
        index_a = (2 * current_index) + 1
        index_b = (2 * current_index) + 2
        if index_b < length_of_list:
            current_less_than_child_a = the_heap[current_index][VALUE_INDEX] <= the_heap[index_a][VALUE_INDEX]
            current_less_than_child_b = the_heap[current_index][VALUE_INDEX] <= the_heap[index_b][VALUE_INDEX]
            if current_less_than_child_a and current_less_than_child_b:
                return temp
            else:
                smaller_index = _index_of_smaller(the_heap, index_a, index_b)
                _swap(the_heap, current_index, smaller_index)
                current_index = smaller_index
        else:
            if index_a < length_of_list:
                if the_heap[current_index][VALUE_INDEX] > the_heap[index_a][VALUE_INDEX]:
                    _swap(the_heap, current_index, index_a)
            return temp
    return temp           


def internal_heapsort(hlist, ribbon):
    """ Performs the heapsort on the list. """
    result = []
    the_heap = []
    for index in range(0, len(hlist)):
        input_value = hlist[index]
        insert(the_heap, input_value, ribbon)

    while len(the_heap) > 0: 
        result.append(remove_minimum_element(the_heap))

    return result


def validate_heaplist(hlist):
    """ Validates the input argument. """
    hlist_not_none = hlist is not None
    passed = hlist_not_none
    return passed


def heapsort(hlist, ribbon):
    """ Performs a heapsort on hlist. Returns None if hlist is None."""
    result = None
    try:
        if validate_heaplist(hlist):
            # creates a working copy of the input argument,
            # so changes are not affecting the input.
            working_copy = list(hlist)
            result = internal_heapsort(working_copy, ribbon)
    except Exception as e:
        print(e)
        result = None
    return result

# -----------END HEAP SORT---------------------


def get_index(row, column, num_cols):
    return (row * num_cols) + column


def get_column(index, num_cols):
    return index % num_cols


def get_row(index, num_cols):
    return int(index / num_cols)


def get_value(ribbon, line_index, num_cols):
    row = get_row(line_index, num_cols)
    col = get_column(line_index, num_cols)
    return ribbon[row][col]


def linear_index(row, col, num_cols):
    return (row * num_cols) + col


def flatten(ribbon):
    m = len(ribbon)
    n = len(ribbon[0])
    result = []
    try:
        for index in range(0, m * n):
            row = get_row(index, n)
            col = get_column(index, n)
            item = ribbon[row][col]
            
            result.append((row, col, item))
            
    except Exception as ex:
        print(ex)
    return result


def print_values(item_list):
    for index in range(0, len(item_list)):
        print(item_list[index][VALUE_INDEX], end=", ")
    print("")


class Trail:
    ''' Class representing the items of the trail table. '''
    def __init__(self, total=0, trail=[]) -> None:
        self.total = total
        self.trail = trail

    def append(self, item):
        self.trail.append(item)
        self.total += item[VALUE_INDEX]
    
    def get_last_item(self):
        return self.trail[len(self.trail) - 1]
    
    def is_valid_next_stop(self, item, ribbon):
        m = len(ribbon)
        n = len(ribbon[0])
        last_item = self.get_last_item()
        is_increasing_value = last_item[VALUE_INDEX] < item[VALUE_INDEX]
        same_row = (last_item[ROW_INDEX] == item[ROW_INDEX])
        same_col = (last_item[COL_INDEX] == item[COL_INDEX])
        is_last_top = (last_item[ROW_INDEX] == 0)
        is_last_bottom = (last_item[ROW_INDEX] == (m - 1))
        up_one = last_item[ROW_INDEX] == item[ROW_INDEX] + 1
        down_one = last_item[ROW_INDEX] == item[ROW_INDEX] - 1
        left_one = last_item[COL_INDEX] == (item[COL_INDEX] + 1) % n
        right_one = last_item[COL_INDEX] == (item[COL_INDEX] - 1) % n
        item_above = (not is_last_top and up_one and same_col)
        item_below = (not is_last_bottom and down_one and same_col)
        item_left = (same_row and left_one)
        item_right = (same_row and right_one)
        is_adjacent = (item_above or item_below or item_left or item_right)
        return (is_increasing_value and is_adjacent)


def append_to_trails(trails, item, ribbon):
    
    if len(trails) == 0:
        new_trail = Trail(item[VALUE_INDEX], [item])
        trails.append(new_trail)
    else:
        for trail in trails:
            if trail.is_valid_next_stop(item, ribbon):
                trail.append(item)
        new_trail = Trail(item[VALUE_INDEX], [item])
        trails.append(new_trail)
    return trails


def make_trails(sorted_list, ribbon):
    trails = []
    for index in range(0, len(sorted_list)):
        # if sorted_list[index][VALUE_INDEX] > 0:
        trails = append_to_trails(trails, sorted_list[index], ribbon)
    return trails


def find_longest_trail(trails):
    result = None
    max = -999
    result_index = -1
    for index in range(0, len(trails)):
        if len(trails[index].trail) > max and len(trails[index].trail) >= 2:
            max = len(trails[index].trail)
            result_index = index
    if result_index != -1:
        result = trails[result_index]
    return result


def package_result(list_of_items):
    result = []
    for index in range(0, len(list_of_items)):
        result.append((list_of_items[index][ROW_INDEX], list_of_items[index][COL_INDEX]))
    return tuple(result)


def internal_longest_path(ribbon):
    result = ()
    flat_list = flatten(ribbon)
    sorted_list = heapsort(flat_list, ribbon)
    trails = make_trails(sorted_list, ribbon)
    longest = find_longest_trail(trails)
    if longest is not None:
        result = package_result(longest.trail)
    return result


def validate(ribbon):
    assert (ribbon is not None)
    assert (len(ribbon) > 0)
    assert (len(ribbon[0]) > 0)
    return


# fill in your code
def longest_path(ribbon):
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
