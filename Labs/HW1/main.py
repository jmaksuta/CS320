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


# calculates the middle index of the sequence.
def get_middle_index(pattern):
    endIndex = int(len(pattern) / 2)
    isEven = len(pattern) % 2 == 0
    if (not isEven):
        endIndex += 1

    return endIndex


def get_result(pattern, isPalindrome, indexToRemove):
    result = None
    if (isPalindrome):
        result = pattern
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
