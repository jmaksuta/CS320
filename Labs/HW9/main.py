"""
Lab 09 - HW9
67.2 Implementing a Trie
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

class Trie:
    def __init__(self, is_word):
        self.is_word = is_word # notes if this node is, itself, a word as well as a possible prefix
        self._children = {} # children are a dictionary

# You need to implement the following methods:
    def add(self, key):
        exists = key in self._children
        # add(key) adds a string to the trie.

        # Returns True if the key was not already in the trie and
        # False if the key is a duplicate or was None or the empty string.
        return (key is not None and not exists)

    def add_keys(tuple_of_keys):
        # add_keys(tuple_of_keys) adds all the keys in the passed tuple to the trie (think of this as a bulk add()). It returns a count of
        # the number of keys successfully added, with 0 (zero) indicating that no keys were added or the tuple was empty or None. If an
        # element of the tuple is None, it is treated as a duplicate string (already in the trie, so no action required).
        pass

    def remove(key):
        # remove(key) removes a key. Returns True if the key was present and False if the key was not present or was None or the
        # empty string.
        pass

    def find(word):
        # find(word) returns True if the word is in the trie and False if the word is not in the trie or the word is None or the empty string.
        pass

    def partial(prefix):
        # partial(prefix) returns a set of all words that begin with the string in prefix. Returns an empty set if the prefix is not present
        # or the prefix is None. Note that an empty string is a valid prefix and should result in partial() returning all words in the tree.
        pass