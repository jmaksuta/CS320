# Determine if a tuple can be made into a palindrome by removing exactly one
# element

# An example import. Delete or replace as desired. Be careful with what
# libraries you use:
# Non-default python libraries may not work in Zybooks.
# import math

# Subroutines if any, go here
def get_palindrome(pattern):
    endIndex = get_middle_index(pattern)

    indexOfElementRemoved = -1
    isPalindrome = True

    for n in range(0, endIndex):
        indexStart = n
        indexEnd = len(pattern)-(n + 1)
        compareResult = compare_elements(pattern,
                                         indexStart,
                                         indexEnd,
                                         indexOfElementRemoved)
        pattern = compareResult[0]
        isPalindrome = compareResult[1]
        indexOfElementRemoved = compareResult[2]

        if not isPalindrome:
            break

    return get_result(pattern, isPalindrome, indexOfElementRemoved)
    # if (isPalindrome):
    #     result = removeElementFromTuple(pattern, indexOfElementRemoved)
    # #make the palindrome and return it
    # return result


def get_middle_index(pattern):
    endIndex = int(len(pattern) / 2)
    isEven = len(pattern) % 2 == 0
    if (not isEven):
        endIndex += 1

    return endIndex


def get_result(pattern, isPalindrome, indexToRemove):
    result = None
    if (isPalindrome):
        result = pattern  # removeElementFromTuple(pattern, indexToRemove)
    return result


def removeElementFromTuple(pattern, indexToRemove):
    theList = list(pattern)
    if (indexToRemove != -1):
        theList.pop(indexToRemove)

    return tuple(theList)


def compare_elements(pattern, indexStart, indexEnd, indexOfElementRemoved):
    canRemove = indexOfElementRemoved == -1
    elementsMatch = True

    start = pattern[indexStart]
    end = pattern[indexEnd]

    indexStartNext = indexStart + 1
    indexEndNext = len(pattern)-(indexStart + 2)

    startNext = pattern[indexStartNext]
    endNext = pattern[indexEndNext]
    if (start == end):
        # its still a palindrome
        pass
    elif (canRemove and startNext == end):
        # its not a palindrome, but lets remove start and check startNext
        # against end
        indexOfElementRemoved = indexStart
        pattern = removeElementFromTuple(pattern, indexOfElementRemoved)
    elif (canRemove and endNext == start):
        # its not a palindrome, but lets remove end and check endNext
        # against start
        indexOfElementRemoved = indexEnd
        pattern = removeElementFromTuple(pattern, indexOfElementRemoved)
    else:
        # this is not a palindrome
        elementsMatch = False

    # print("start={s}, end={e}".format(s=start, e=end))
    return (pattern, elementsMatch, indexOfElementRemoved)


# Fill in find_palindrome
def find_palindrome(pattern):
    result = None
# Your task is to write a routine: find_palindrome(pattern) which takes
# a tuple and returns a tuple or None.
    if (len(pattern) > 2):
        result = get_palindrome(pattern)
    return result
# The returned tuple must be a palindrome which results from removing just
# one element from pattern.
# So, for instance, if pattern was (3, 2, 1, 1, 2, 4, 3), the returned tuple
# would be (3, 2, 1, 1, 2, 3).
# If more than one element must be removed from the tuple to make a
# palindrome, or a palindrome is not possible,
# then find_palindrome() returns None.

# A few special cases:

# No trivial (single element) palindromes. The returned palindrome must be of
# length 2 or longer. If pattern is too short to result in a palindrome of
# length 2 or pattern is None, return None.
# No throwing exceptions (they confuse zybooks). If there are other bad input
# conditions not discussed here, return None.
# No modifying elements in pattern. So if pattern is ("ab", "a", "a"), do not
# return ("a", "a", "a").
# No moving elements within pattern. The only permissible change to get a new
# pattern is to remove one element.
# pattern may already be a palindrome, in which case you need to see if a
# there is a way to remove one element and get a new palindrome.

# test code:
# print(find_palindrome(("t", "e", "s", "t")))
# print(find_palindrome(("t", "e", "s", "t", "e", "r")))

# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)))
# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)) == (3, 2, 1, 1, 2, 3))
