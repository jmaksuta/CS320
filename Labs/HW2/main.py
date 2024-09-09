"""
Lab 02 - HW2
60.2 Lab 2: New Words
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""


# compares two words for equality
def compare_words(search_for, compare_to):
    return search_for.lower() == compare_to.lower()


# Returns true if input_word is greater than compare_to.
def is_greater_than(input_word, compare_to):
    return input_word.lower() > compare_to.lower()


# Calculates the middle index of the array
def calculate_middle(low, high):
    return int((high + low) / 2)


# Performs a O(log n) binary search operation on wordlist looking for word.
def binary_search(word, wordlist):
    result = None
    
    low = 0
    high = len(wordlist) - 1
    middle = calculate_middle(low, high)
    
    while (high >= low):
        search_for_word = word
        search_in_word = wordlist[middle]
        if (compare_words(search_for_word, search_in_word)):
            result = word
            break
        else:
            if is_greater_than(search_for_word, search_in_word):
                low = middle + 1
            else:
                high = middle - 1
            middle = calculate_middle(low, high)

    return result


# this is the main function internally, that runs the loop and search
def internal_new_words(words, wordlist):
    result = None
    list = []
    for word in words:
        if binary_search(word, wordlist) is None:
            list.append(word)

    if len(list) > 0:
        result = tuple(list)
    return result


# validates the input arguments
def validate(words, wordlist):
    assert words is not None
    assert wordlist is not None
    assert type(words) is tuple
    assert type(wordlist) is tuple
    return


# your subroutine goes here
def new_words(words, wordlist):
    result = None
    try:
        validate(words, wordlist)
        result = internal_new_words(words, wordlist)

    except Exception as ex:
        print(ex)
        result = None
    return result
