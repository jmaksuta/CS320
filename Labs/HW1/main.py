# Determine if a tuple can be made into a palindrome by removing exactly one
# element

# Subroutines if any, go here
def get_palindrome(pattern):
    endIndex = get_middle_index(pattern)

    indexOfElementRemoved = -1
    isPalindrome = True

    for n in range(0, endIndex):
        indexStart = n
        indexEnd = len(pattern)-(n + 1)
        processResult = process_elements(pattern,
                                         indexStart,
                                         indexEnd,
                                         indexOfElementRemoved)
        pattern = processResult[0]
        isPalindrome = processResult[1]
        indexOfElementRemoved = processResult[2]

        if not isPalindrome:
            break

    return get_result(pattern, isPalindrome)


# calculates the middle index of the sequence.
def get_middle_index(pattern):
    endIndex = int(len(pattern) / 2)
    isEven = len(pattern) % 2 == 0
    if (not isEven):
        endIndex += 1

    return endIndex


def get_result(pattern, isPalindrome):
    result = None
    if (isPalindrome):
        result = pattern
    return result


def removeElementFromTuple(pattern, indexToRemove):
    theList = list(pattern)
    if (indexToRemove != -1):
        theList.pop(indexToRemove)
    return tuple(theList)


def process_elements(pattern, indexStart, indexEnd, indexOfElementRemoved):
    canRemove = indexOfElementRemoved == -1
    elementsMatch = True

    start = pattern[indexStart]
    end = pattern[indexEnd]

    indexStartNext = indexStart + 1
    indexEndNext = len(pattern)-(indexStart + 2)

    startNext = pattern[indexStartNext]
    endNext = pattern[indexEndNext]

    indexToRemove = get_index_to_remove(canRemove,
                                        start,
                                        end,
                                        indexStart,
                                        indexEnd,
                                        startNext,
                                        endNext)
    canRemove = indexToRemove != -1
    elementsMatch = matches(start, end) or canRemove
    if (canRemove):
        pattern = removeElementFromTuple(pattern, indexToRemove)
        indexOfElementRemoved = indexToRemove

    return (pattern, elementsMatch, indexOfElementRemoved)


def matches(start, end):
    return (start == end)


def get_index_to_remove(canRemove, start, end, indexStart,
                        indexEnd, startNext, endNext):
    indexToRemove = -1
    if (canRemove and startNext == end):
        indexToRemove = indexStart
    elif (canRemove and endNext == start):
        indexToRemove = indexEnd
    return indexToRemove


# Finds a palindrome and returns None if none found, otherwise returns the
# palindrome tuple.
def find_palindrome(pattern):
    result = None
    if (len(pattern) > 2):
        result = get_palindrome(pattern)
    return result


# test code:
# print(find_palindrome(("t", "e", "s", "t")))
# print(find_palindrome(("t", "e", "s", "t", "e", "r")))

# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)))
# print(find_palindrome((3, 2, 1, 1, 2, 4, 3)) == (3, 2, 1, 1, 2, 3))
