"""
Lab 01 - HW1
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""
# Determine if a tuple can be made into a palindrome by removing exactly one
# element

# Subroutines if any, go here


# this function gets the palindrome.
def get_palindrome(the_pattern):
    # this function gets the palindrome.
    end_index = get_middle_index(the_pattern)

    index_of_removed_element = -1
    is_palindrome = True

    for start_index in range(0, end_index):
        end_index = len(the_pattern)-(start_index + 1)
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
    end_index = int(len(the_pattern) / 2)
    is_even = len(the_pattern) % 2 == 0
    if (not is_even):
        end_index += 1

    return end_index


def get_result(the_pattern, is_palindrome):
    result = None
    if (is_palindrome):
        result = the_pattern
    return result


def remove_element_from_tuple(the_pattern, index_to_remove):
    the_list = list(the_pattern)
    if (index_to_remove != -1):
        the_list.pop(index_to_remove)
    return tuple(the_list)


def process_elements(the_pattern, start_index, end_index,
                     index_of_removed_element):
    can_remove = index_of_removed_element == -1
    elements_match = True

    start = the_pattern[start_index]
    end = the_pattern[end_index]

    next_start_index = start_index + 1
    next_end_index = len(the_pattern)-(start_index + 2)

    start_next = the_pattern[next_start_index]
    end_next = the_pattern[next_end_index]

    index_to_remove = get_index_to_remove(can_remove,
                                          start,
                                          end,
                                          start_index,
                                          end_index,
                                          start_next,
                                          end_next)
    can_remove = index_to_remove != -1
    elements_match = matches(start, end) or can_remove
    if (can_remove):
        the_pattern = remove_element_from_tuple(the_pattern, index_to_remove)
        index_of_removed_element = index_to_remove

    return (the_pattern, elements_match, index_of_removed_element)


def matches(start, end):
    return (start == end)


def get_index_to_remove(can_remove, start, end, start_index,
                        end_index, start_next, end_next):
    index_to_remove = -1
    if (can_remove and start_next == end):
        index_to_remove = start_index
    elif (can_remove and end_next == start):
        index_to_remove = end_index
    return index_to_remove


def find_palindrome(pattern):
    """Finds a palindrome and returns None if none found,
    otherwise returns the palindrome tuple."""
    result = None
    if (len(pattern) > 2):
        result = get_palindrome(pattern)
    return result


# test code:
# print(find_palindrome(("t", "e", "s", "t")))
# print(find_palindrome(("t", "e", "s", "t", "e", "r")))

# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)))
# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)) == (3, 2, 1, 1, 2, 3))
