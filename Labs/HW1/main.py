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

    return get_result(the_pattern, is_palindrome)


# calculates the middle index of the sequence.
def get_middle_index(the_pattern):
    end_index = int(len(the_pattern) / 2) - 1
    is_even = len(the_pattern) % 2 == 0
    if (not is_even):
        end_index += 1

    return end_index


# Returns the the pattern if it is a palindrome, otherwise returns None
def get_result(the_pattern, is_palindrome):
    result = None
    if (is_palindrome):
        result = the_pattern
    return result


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
        can_remove = index_to_remove != -1
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
    if (len(pattern) > 1):
        result = get_palindrome(pattern)
    return result
