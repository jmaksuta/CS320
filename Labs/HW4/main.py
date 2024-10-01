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

def find_larger_prime(larger_than):
    return 11

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

def internal_longest_path(ribbon):
    result = ()
    min_max = find_min_max(ribbon)
    min = min_max[0]
    max = min_max[1]
    hash_table = make_hash(ribbon, 91, max)

    m = len(ribbon)
    n = len(ribbon[0])
    for index in range(0, m * n):
        row = get_row(index, n)
        col = get_column(index, n)
        item = ribbon[row][col]
        print(item)
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

    except (AssertionError):
        result = None
    return result


# testing
# print(longest_path(((),())))
# print(longest_path(((),)))
# print(longest_path(()))
longest_path(((1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)))

longest_path(((1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)))

