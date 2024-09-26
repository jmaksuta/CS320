"""
Lab 03 - HW3
61.2 Lab 3: Heap Sort
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""


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


def insert(the_heap, element=None) -> None:
    """ Inserts an element into the heap and heapifys. """
    the_heap.append(element)
    last_index = len(the_heap) - 1
    current_index = last_index
    while current_index > 0 and _greater_than(the_heap[int((current_index - 1) / 2)],
                                              the_heap[current_index]):
        parent_index = int((current_index - 1) / 2)
        child_index = current_index
        _swap(the_heap, parent_index, child_index)
        current_index = parent_index
    return


def _index_of_smaller(the_heap, index_a, index_b):
    """ Compares element at index_a with element at index_b and
    returns the index of the smaller of the two."""
    result = -1
    if the_heap[index_a] <= the_heap[index_b]:
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
    # the_heap = the_heap[:length_of_list]
    del the_heap[length_of_list]
    current_index = 0
    while current_index < length_of_list:
        index_a = (2 * current_index) + 1
        index_b = (2 * current_index) + 2
        if index_b < length_of_list:
            current_less_than_child_a = the_heap[current_index] <= the_heap[index_a]
            current_less_than_child_b = the_heap[current_index] <= the_heap[index_b]
            if current_less_than_child_a and current_less_than_child_b:
                return temp
            else:
                smaller_index = _index_of_smaller(the_heap, index_a, index_b)
                _swap(the_heap, current_index, smaller_index)
                current_index = smaller_index
        else:
            if index_a < length_of_list:
                if the_heap[current_index] > the_heap[index_a]:
                    _swap(the_heap, current_index, index_a)
            return temp
    return temp           


def internal_heapsort(hlist):
    """ Performs the heapsort on the list. """
    result = []
    the_heap = []
    for index in range(0, len(hlist)):
        input_value = int(hlist[index])
        insert(the_heap, input_value)

    # length = len(the_heap)
    # for index in range(len(the_heap)):
    while len(the_heap) > 0: 
        result.append(remove_minimum_element(the_heap))

    return result


def validate(hlist):
    """ Validates the input argument. """
    hlist_not_none = hlist is not None
    passed = hlist_not_none
    return passed


def heapsort(hlist):
    """ Performs a heapsort on hlist. Returns None if hlist is None."""
    result = None
    try:
        if validate(hlist):
            # creates a working copy of the input argument,
            # so changes are not affecting the input.
            working_copy = list(hlist)
            result = internal_heapsort(working_copy)
    except Exception as e:
        result = None
    return result
