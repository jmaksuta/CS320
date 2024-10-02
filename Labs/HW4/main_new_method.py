import math

# 62.2
# Longest Path
# The challenge in this assignment is to find the longest path of increasing values in a matrix.
# To make the problem a little more challenging, we are making the matrix a looped ribbon, in which
# on the x-axis, the last element is adjacent to the first.
# We start by defining a path, trail, as a tuple of (x, y) values, each of which is a
# position in matrix ribbon.
# In a valid path:
# any (x, y) value appears at most once;
# if trail[t] = (x1, y1) and trail[t+1] = (x2, y2),
# then position (x2, y2) must be adjacent to (x1, y1),
# where adjacent is defined to mean, above
# (e.g. y1 < y2 and x1 == x2), below, to the left, or to the right of (x1, y1);
# and if trail[t] = (x1, y1) and trail[t+1] = (x2, y2),
# then ribbon[x1, y1] < ribbon[x2, y2].
#
# To make things a bit more exciting, we make the matrix ribbon
# into a looped ribbon by connecting the leftmost and rightmost columns.
# Thus, if ribbon is an m by n matrix, then ribbon[x1,0] is to the right
# of ribbon[x1 ,n-1]. Note that this is not true in the x dimension
# -- there is no neighbor above above ribbon[0,y1] and no neighbor below ribbon[m-1,y1].
# 
# Your task is to write a routine longest_path(ribbon)
# which returns the longest path of increasing values in the ribbon.
# The input, ribbon is a matrix (tuple of tuples) of m rows and n columns,
# where each entry contains a numerical value (which may be negative).
# The returned path is the tuple of (x, y) coordinates in the path.
# Some details:
# * - The top and bottom of the matrix are boundaries that cannot be crossed (you cannot go above line 0 or below line m-1).
# * - The matrix is row-based. That is ribbon[0] is a tuple with all the elements in row 0.
#     You may assume that all rows are the same length as the first row in the tuple.
# * - If there are multiple paths of equal length, any of them may be returned.
# * - The path is a tuple of (x, y) tuples. (So the path is of the form ((x1, y1), (x2,y2), ... ).
# * - The path must start with the (x, y) coordinates with the lowest value in the path.
# * - A path must have at least two elements. If there are no valid paths, return ()
# DONE * - If ribbon is None or has an m or n dimension that is 0, return None.
#
#
# Performance Expectations
# This problem is straightforward (albeit with some minor challenges) if you don't worry about
# performance. But we are requiring you to worry about performance.
# Define N = m*n, the total number of elements in the ribbon. We are looking for a solution that is
# O(N).
# Hints:
# trail does not necessarily contain the largest or smallest value in ribbon.
# The trick is to find a solution that provably explores all possible paths from any position in
# (e.g. ribbon[x, y]) a constant number of times.
# Python Tips
# Some python programming tips that may or may not be useful, depending on the solution you
# choose.
# Reminder that, for a tuple of length m, tuple[-1] is a reference to the position tuple[m-1].

# subroutines if any, go here
# algorithm L from knuth for permutation
# returns None if no permutations possible


#-----------BEGIN HEAP SORT-------------------


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

#-----------END HEAP SORT---------------------

def algL(list):
    if ((list is None) or (len(list) <= 1)):
        return None

    n = len(list)

    #  differs from Knuth as Knuth indexes arrays from 1 rather than 0
    j = n - 2

    while ((j >= 0) and (list[j] >= list[j+1])):
        j -= 1

    if (j == -1):
        return None

    # flip adjacent positions
    f = n - 1
    while (list[j] >= list[f]):
        f -= 1

    temp = list[f]
    list[f] = list[j]
    list[j] = temp

    # now put everything past the flip in sorted order
    f = n-1
    k = j + 1
    while (k < f):
        temp = list[k]
        list[k] = list[f]
        list[f] = temp
        k += 1
        f -= 1

    return list




class Item:
    ''' Class representing the items of the ribbon. '''
    def __init__(self, value=0, row=None,col=None) -> None:
        self.value = value
        self.row = row
        self.col = col

def universal_hash(key, a, b, N, m):
    return ((((a * key) + b) % N) % m)

def get_index(row, column, num_cols):
    return (row * num_cols) + column

def get_column(index, num_cols):
    return index % num_cols

def get_row(index, num_cols):
    return int(index / num_cols)

def find_min_max(ribbon):
    min = 0
    max = 0
    m = len(ribbon)
    n = len(ribbon[0])
    for index in range(0, m * n):
        row = get_row(index, n)
        col = get_column(index, n)
        item = ribbon[row][col]
        if (item > max):
            max = item
        if (item < min):
            min = item
    return (min, max)

def internal_longest_path(ribbon):
    result = ()
    m = len(ribbon)
    n = len(ribbon[0])
    for index in range(0, m * n):
        row = get_row(index, n)
        col = get_column(index, n)
        item = ribbon[row][col]
        print(item)
    return result

def iterate_ribbon(ribbon):
    result = ()
    m = len(ribbon)
    n = len(ribbon[0])
    for index in range(0, m * n):
        row = get_row(index, n)
        col = get_column(index, n)
        item = ribbon[row][col]
        print(item)
    return result

def is_prime(number):
    result = False
    flag = True
    for value in range(2, int(math.sqrt(number) + 1)):
        if number % value == 0:
            flag = False
            break
    if flag and number > 0:
        result = True
    return result

# /**
#  * This function takes the reference to the array and the array size as an input.
#  * You need to iterate over the elements of the array and check if how many primes they contain.
#  * Return the number of primes counted.
#  */
# int *make_prime_array(int nth, int *array)
# {
#     int prime_count = 0;
#     // prime series doesn't include 1 in document.
#     int current = 2;
#     while (prime_count < nth)
#     {
#         if (is_prime(current))
#         {
#             array[prime_count] = current;
#             prime_count++;
#         }
#         current++;
#     }

#     return array;
# }

def find_larger_prime(larger_than):
    found = False
    even = (larger_than % 2 == 0)
    value = larger_than + (1 if even else 2)
    while (not found):
        value += 2
        found = is_prime(value)
    return value

def make_hash(ribbon, the_prime, table_size):
    result = [[]] * table_size
    try:
        m = len(ribbon)
        n = len(ribbon[0])
        for index in range(0, m * n):
            row = get_row(index, n)
            col = get_column(index, n)
            item = ribbon[row][col]
            the_item = Item(item, row, col)

            hash = universal_hash(item, 1, 0, the_prime, table_size)
            
            result[hash].append(the_item)
            # result[hash] = Item(item, row, col)
    except Exception as ex:
        print(ex)
    return result

class Element:
    ''' Class representing the items of the trail table. '''
    def __init__(self, index=-1, value=0) -> None:
        self.index = index
        self.value = value

class ElementTrail:
    def __init__(self, total=0, list=[]) -> None:
        self.total = total
        self.list = list

    def addElement(self, element=None) -> None:
        self.total += element.value
        self.list.append(element.index)

    def get_last_element(self):
        result = None
        length = len(self.list)
        if length > 0:
            result = self.list[length - 1]
        return result

class TrailItem:
    ''' Class representing the items of the trail table. '''
    def __init__(self) -> None:
        self.total = 0
        self.trail = []

    def append(self, index, value):
        self.trail.append(index)
        self.total += value

    def appendTrail(self, trail_item):
        self.trail = trail_item.trail + self.trail
        self.value += trail_item.value


class TrailItemGroup:
    ''' Class representing the items of the trail table. '''
    def __init__(self, num_cols) -> None:
        self.total = 0
        self.trail = [TrailItem(),TrailItem(),TrailItem()]

    def append(self, index, value):
        self.trail[0].append(index, value)
        self.trail[1].append(index, value)
        self.trail[2].append(index, value)

def build_trail_table(ribbon):
    m = len(ribbon)
    n = len(ribbon[0])
    table_size = m * n
    result = [TrailItemGroup(n)] * table_size
    
    for index in range(0, (table_size - n) + 1):
        row = int(index / n)
        col = index % n
        value = ribbon[row][col]

        result[index].append(index, value)

        child_row = row + 1
        left_index = (child_row * n) + (((col - 1) + n) % n)
        bottom_index = (child_row * n) + (col)
        right_index = (child_row * n) + (((col + 1) - n) % n)

        my_left_trail = result[index].trail[0]
        my_center_trail = result[index].trail[1]
        my_right_trail = result[index].trail[2]

        result[left_index].trail[2].append( index, value)
        result[bottom_index].trail[1].append(index, value)
        result[right_index].trail[0].append(index, value)

        # left = ribbon[row + 1][((col - 1) + n) % n]
        # bottom = ribbon[row + 1][col]
        # right = ribbon[row + 1][((col + 1) - n) % n]

        # left.append(index)
        # bottom.append(index)
        # right.append(index)

    return result

def in_bounds(n_index, left, right):
    result = False
    if left < right:
        result = (n_index >= left and n_index <= right)
    else:
        result = (n_index >= left or n_index <= right)
    return result

def append_trails(lists, element, num_cols):
    result = []
    for a_list in lists:
        new_list = []
        # new_list += a_list
        last_elem = a_list.get_last_element()
        # last_elem = a_list[len(a_list.list) - 1]
        l_bound = ((last_elem - 1) + num_cols) % num_cols
        r_bound = ((last_elem + 1) - num_cols) % num_cols
        n_index = element.index % num_cols
        if in_bounds(n_index, l_bound, r_bound):
            new_group = ElementTrail(a_list.total, list(a_list.list))
            new_group.addElement(element)
            result.append(new_group)
            # new_list[:] = a_list
            # new_list.append(element_index)
            # result.append(new_list)

        # result.append(a_list + element_index)
        # a_list.append(element_index)
    return result

def linear_index(row, col, num_cols):
    return (row * num_cols) + col

def make_trails(ribbon, trails, current_row, left_Bound, length):
    result = []
    m = len(ribbon)
    n = len(ribbon[0])
    new_trails = trails
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
    table_length = (m * n)

    result = []
    for index in range(0, n):
        trails = []
        current_row = 0
        left_Bound = index
        right_bound = index
        while current_row < m:
            if current_row == 0:
                # add the index to the trail
                l_index = linear_index(current_row, index, n)
                value = ribbon[current_row][index]
                # element = Element(l_index, value)
                group = ElementTrail(value, [l_index])
                # group.addElement(element)
                trails.append(group)
                # trails.append(TrailItemGroup()[index])
            else:
                left_Bound = ((index - ((current_row - 1) + 1)) + n) % n
                right_bound = ((index + ((current_row - 1) + 1)) - n) % n
                length = ((index + ((current_row - 1) + 1)) - (index - ((current_row - 1) + 1))) + 1
                trails = make_trails(ribbon, trails, current_row, left_Bound, length)
            current_row += 1
        result += trails
    return result    



def get_permutation(ribbon, start_column_index):
    # index = start_column_index
    m = len(ribbon)
    n = len(ribbon[0])
    table_length = (m * n)
    current_row = 0
    trails = [[],] * n
    
    for index in range(0, table_length):
        col = index % n
        row = int(index / n)




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

def find_max_group(trail_groups):
    result = None
    max = 0
    for index in range(0, len(trail_groups)):
        group = trail_groups[index]
        if group.total > max:
            max = group.total
            result = group
    return result


def internal_longest_path(ribbon):
    result = ()
    flat_list = flatten(ribbon)
    
    # groups = make_all_trails(ribbon)
    # max_group = find_max_group(groups)
    # if max_group != None:
    #     result = tuple(max_group.list)

    # result = get_permutation(ribbon, 0)
    # flat_matrix = flatten(ribbon)
    # set = flat_matrix
    # while (set != None):
    #     print(set)
    #     set = algL(set)
    # min_max = find_min_max(ribbon)
    # min = min_max[0]
    # max = min_max[1]
    # the_prime = find_larger_prime(max)
    # trail_table = build_trail_table(ribbon)
    # hash_table = make_hash(ribbon, the_prime, max)

    # the_list = []
    # for index in range(0, len(hash_table) + 1):
    # # m = len(ribbon)
        
    #     item = hash_table[0][index]
    #     the_list.append((item.row, item.col))
    #     print("index={index},value={value}, col={col}, row={row}".format(index=index,value=item.value, row=item.row, col=item.col))

    # if (len(the_list) > 0):
    #     result = tuple(the_list)
    # m = len(ribbon)
    # n = len(ribbon[0])
    # for index in range(0, m * n):
    #     row = get_row(index, n)
    #     col = get_column(index, n)
    #     item = ribbon[row][col]
        # print(item)
    return result

def validate(ribbon):
    assert(ribbon is not None)
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


# testing
# print(longest_path(((),())))
# print(longest_path(((),)))
# print(longest_path(()))
print(longest_path(((1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5))))

# print(longest_path(((1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5))))

