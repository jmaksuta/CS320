"""
Lab 03 - HW3
61.2 Lab 3: Heap Sort
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

heap_list = []

# class Heap:
#     ''' Class representing the heap in a heap sort. '''
#     def __init__(self) -> None:
#         self.list = []

def _swap(self, up_elem_index, down_elem_index):
    """ swaps the elements in the list at indices up_elem_index
    and down_elem_index. """
    temp = self.list[up_elem_index]
    self.list[up_elem_index] = self.list[down_elem_index]
    self.list[down_elem_index] = temp
    return

def _greater_than(self, left_operand, right_operand):
    """ Returns True if left_operand is greater than right_operand. """
    return left_operand > right_operand

def insert(self, element=None) -> None:
    """ Inserts an element into the heap and heapifys. """
    self.list.append(element)
    last_index = len(self.list) - 1
    current_index = last_index
    while current_index > 0 and self._greater_than(self.list[int((current_index - 1) / 2)],
                                                    self.list[current_index]):
        parent_index = int((current_index - 1) / 2)
        child_index = current_index
        self._swap(parent_index, child_index)
        current_index = parent_index
    return

def _index_of_smaller(self, index_a, index_b):
    """ Compares element at index_a with element at index_b and
    returns the index of the smaller of the two."""
    result = -1
    if self.list[index_a] <= self.list[index_b]:
        result = index_a
    else:
        result = index_b
    return result

def _to_index(self, nth_value):
    """ Returns the index value an the nth value.
    i.e. the nth element has an index n - 1. """
    return nth_value - 1

def _nth_elem(self, n):
    """ Returns the nth element. """
    return self.list[self._to_index(n)]

def remove_minimum_element(self):
    """ Removes the minimum element from the heap, the first element,
    and heapifys"""
    temp = self.list[0]
    length_of_list = len(self.list)
    self.list[0] = self._nth_elem(length_of_list)
    length_of_list = length_of_list - 1
    self.list = self.list[:length_of_list]
    current_index = 0
    while current_index < length_of_list:
        index_a = (2 * current_index) + 1
        index_b = (2 * current_index) + 2
        if index_b < length_of_list:
            current_less_than_child_a = self.list[current_index] <= self.list[index_a]
            current_less_than_child_b = self.list[current_index] <= self.list[index_b]
            if current_less_than_child_a and current_less_than_child_b:
                return temp
            else:
                smaller_index = self._index_of_smaller(index_a, index_b)
                self._swap(current_index, smaller_index)
                current_index = smaller_index
        else:
            if index_a < length_of_list:
                if self.list[current_index] > self.list[index_a]:
                    self._swap(current_index, index_a)
            return temp
    return temp      


def internal_heapsort(hlist):
    """ Performs the heapsort on the list. """
    result = []
    heap_list = []
    for index in range(0, len(hlist)):
        input_value = int(hlist[index])
        insert(input_value)

    for index in range(len(heap_list)):
        result.append(str(remove_minimum_element()))

    return result


def validate(hlist):
    """ Validates the input argument. """
    hlist_not_none = hlist is not None
    passed = hlist_not_none
    return passed


def heapsort(hlist):
    """ Performs a heapsort on hlist. Returns None if hlist is None."""
    result = None
    if validate(hlist):
        # creates a working copy of the input argument,
        # so changes are not affecting the input.
        working_copy = list(hlist)
        result = internal_heapsort(working_copy)
    return result
