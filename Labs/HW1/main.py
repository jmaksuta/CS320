"""
Lab 01 - HW1
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""
# Determine if a tuple can be made into a palindrome by removing exactly one
# element

# Subroutines if any, go here


# main internal method, processes the pattern, and gets a result.
def get_palindrome(the_pattern):
    middle_index = get_middle_index(the_pattern)

    index_of_removed_element = -1
    is_palindrome = True

    for start_index in range(0, middle_index + 1):
        end_index = len(the_pattern) - (start_index + 1)
        process_result = process_elements(the_pattern,
                                          start_index,
                                          end_index,
                                          index_of_removed_element)
        the_pattern = process_result[0]
        is_palindrome = process_result[1]
        index_of_removed_element = process_result[2]

        if not is_palindrome:
            break

    return get_result(the_pattern, is_palindrome, index_of_removed_element)


# calculates the middle index of the sequence.
def get_middle_index(the_pattern):
    end_index = int(len(the_pattern) / 2) - 1
    if (not is_even(the_pattern)):
        end_index += 1
    return end_index


# Returns the the pattern if it is a palindrome, otherwise returns None
def get_result(the_pattern, is_palindrome, index_of_removed_element):
    result = None
    elem_was_removed = element_was_removed(index_of_removed_element)
    if (is_palindrome and elem_was_removed):
        result = the_pattern
    elif (is_palindrome and not elem_was_removed):
        result = get_new_palindrome_from_existing(the_pattern)
    if is_trivial(the_pattern):
        result = None
    return result


def element_was_removed(index_of_removed_element):
    return (index_of_removed_element != -1)


def is_trivial(the_pattern):
    return len(the_pattern) < 2

# returns a new palindrome from an existing palindrome
def get_new_palindrome_from_existing(the_pattern):
    # even and odd palindromes can be made into new one by
    # removing a middle index element
    if len(the_pattern) > 2:
        index_to_remove = get_middle_index(the_pattern)
        the_pattern = remove_element_from_tuple(the_pattern, index_to_remove)
    return the_pattern


def is_even(the_pattern):
    return len(the_pattern) % 2 == 0


# Removes the element at specified index from a tuple.
def remove_element_from_tuple(the_pattern, index_to_remove):
    the_list = list(the_pattern)
    if (index_to_remove != -1):
        the_list.pop(index_to_remove)
    return tuple(the_list)


# Returns a tuple after processes the elements of pattern.
def process_elements(the_pattern, start_index, end_index,
                     index_of_removed_element):
    can_remove = index_of_removed_element == -1

    start = the_pattern[start_index]
    end = the_pattern[end_index]

    next_start_index = start_index + 1
    next_end_index = len(the_pattern) - (start_index + 2)

    start_next = the_pattern[next_start_index]
    end_next = the_pattern[next_end_index]

    elements_match = matches(start, end)

    if not elements_match:
        index_to_remove = get_index_to_remove(can_remove, start, end,
                                              start_index, end_index,
                                              start_next, end_next)
        can_remove = (index_to_remove != -1) and (len(the_pattern) - 1 > 1)
        elements_match = can_remove
        remove_result = remove_if_can_match(the_pattern, can_remove,
                                            index_to_remove)
        the_pattern = remove_result[0]
        index_of_removed_element = remove_result[1]

    return (the_pattern, elements_match, index_of_removed_element)


# Returns true if start and end are equivalent, otherwise False.
def matches(start, end):
    return (start == end)


# Returns the index of an element that can be removed to make it match the
# other element.
def get_index_to_remove(can_remove, start, end, start_index,
                        end_index, start_next, end_next):
    index_to_remove = -1
    if (can_remove and start_next == end):
        index_to_remove = start_index
    elif (can_remove and end_next == start):
        index_to_remove = end_index
    return index_to_remove


def remove_if_can_match(the_pattern, can_remove, index_to_remove):
    index_of_removed_element = -1
    if (can_remove):
        the_pattern = remove_element_from_tuple(the_pattern, index_to_remove)
        index_of_removed_element = index_to_remove
    return (the_pattern, index_of_removed_element)


def find_palindrome(pattern):
    """Finds a palindrome and returns None if none found,
    otherwise returns the palindrome tuple."""
    result = None
    try:
        assert(type(pattern) is tuple)
        if (not is_trivial(pattern)):
            result = get_palindrome(pattern)
    except AssertionError:
        result = None
    return result
