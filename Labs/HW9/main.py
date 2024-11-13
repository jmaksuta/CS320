"""
Lab 09 - HW9
67.2 Implementing a Trie
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

# 67.2 Implementing a Trie
# In some applications, such as email, as you type a word, the application will suggest ways to autocomplete it.
# So you might type "for" and have the application suggest "fork" or "form".
# One data structure that can be used to implement this feature is a trie (pronounced "try").
#
# A trie is a type of tree, where a search is done by breaking the key up into segments, sometimes called strides.
# At each node in the tree, you take the next stride in the key and use it as an index into a data structure, usually an array,
# but sometimes a hash table or similar associative data structure, that returns a pointer to the appropriate next child node.
# See section 6.6 of the textbook for more details. In this lab, you are asked to implement the methods for a Python class for a trie.
# The trie stores strings, with each node using the next character in the string as the next stride (index) to find any children.
# Children are stored in a dictionary, where the character is the key and the value is the pointer to the child node.
#
# We have already defined the class and the __init__ method in main.py:
# class Trie:
# def __init__(self, is_word):
# self._is_word = is_word # notes if this node is, itself, a word as well as a possible
# prefix
# self._children = {} # children are a dictionary
#
# You need to implement the following methods:
# add(key) adds a string to the trie. Returns True if the key was not already in the trie and False if the key is a duplicate or
# was None or the empty string.
# add_keys(tuple_of_keys) adds all the keys in the passed tuple to the trie (think of this as a bulk add()). It returns a count of
# the number of keys successfully added, with 0 (zero) indicating that no keys were added or the tuple was empty or None. If an
# element of the tuple is None, it is treated as a duplicate string (already in the trie, so no action required).
# remove(key) removes a key. Returns True if the key was present and False if the key was not present or was None or the
# empty string.
# find(word) returns True if the word is in the trie and False if the word is not in the trie or the word is None or the empty string.
# partial(prefix) returns a set of all words that begin with the string in prefix. Returns an empty set if the prefix is not present
# or the prefix is None. Note that an empty string is a valid prefix and should result in partial() returning all words in the tree.
#
# Tips
# You may add additional fields to the trie structure if you wish
# (remember to add them in init and make sure they are properly initialized to empty values or None as appropriate).
# Also, if you prefer a different structure for trie nodes, you can use a different object below the root of the trie.
# But you must use class Trie for the root of the trie.
#
# Remember that a word can also be a prefix. So if the words "for", "fork", "form" and "forget" are all in the trie,
# the node reached by the string "for", will have _is_word set to True (to say that "for" is a word) and have children for the letters "k", "m" and "g".
# Furthermore, find("for") should return True.
#
# You may need internal helper methods in the class. Reminder that such internal methods should have names starting with an
# underscore ("_").
#
# Unicode strings in Python are iterable. You can iterate over the string or index it. You should not convert the string to a binary string.
# Your code should support any Unicode character.
#
# Cautions
# The textbook describes both tries and compressed tries (which you can think of as tries with variable stride sizes in each node). We are
# asking you to implement a simple trie. If you want to implement variable strides, our test code will accept them.



class Trie:
    def __init__(self):
    # def __init__(self, is_word):
        self.is_word = False # notes if this node is, itself, a word as well as a possible prefix
        self._children = {} # children are a dictionary

    def add(self, key: str) -> bool:
        """ Adds a string to the trie.
        Returns True if the key was not already in the trie and
        False if the key is a duplicate or was None or the empty string. """
        result = False
        if key is None or len(key) == 0 or self.find(key):
            return False
        # exists = False        
        index = 0
        character = key[index]
        exists = character in self._children
        if not result:
            self._children[character] = Trie()
            result = True
        next = key[index + 1:]
        if len(next) > 0:
            result = (result and self._children[character].add(next))
        return result

    def add_keys(self, keys: tuple[str, ...]) -> int:
        """ adds all the keys in the passed tuple to the trie.
        Returns a count of the number of keys successfully added, with 0 (zero)
        indicating that no keys were added or the tuple was empty or None.
        """
        if keys is None or len(keys) == 0:
            return 0
        added_count = 0
        for key in keys:
            is_added = self.add(key)
            if is_added:
                added_count += 1
        # If an element of the tuple is None,
        # it is treated as a duplicate string (already in the trie, so no action required).
        return added_count

    def remove(self, key: str) -> bool:
        """ Removes a key. Returns True if the key was present and
        False if the key was not present or was None or the empty string. """
        
        if key is None or len(key) == 0 or not self.find(key):
            return False
        result = False

        exists = False
        index = 0
        character = key[index]
        result = character in self._children
        if not exists:
            newtrie = Trie()
            self._children[character] = newtrie
        next = key[index + 1:]
        
        if len(next) > 0:
            result = result and self._children[character].add(next)
        return result #(exists and key is not None)

    def find(self, key: str) -> bool:
        """ Returns True if the word is in the trie and
        False if the word is not in the trie or the word is None or the empty string. """
        result = False
        if key is None or len(key) == 0:
            return False
        index = 0
        character = key[index]
        result = character in self._children
        if result:
            next = key[index + 1:]
            if len(next) > 0:
                result = result and self._children[character].find(next)
        # find(word) returns True if the word is in the trie and False if the word is not in the trie or the word is None or the empty string.
        return result

    def partial(self, prefix: str) -> set[str]:
        """ returns a set of all words that begin with the string in prefix.
        Returns an empty set if the prefix is not present or the prefix is None. """
        # partial(prefix) returns a set of all words that begin with the string in prefix. Returns an empty set if the prefix is not present
        # or the prefix is None.
        # Note that an empty string is a valid prefix and should result in partial() returning all words in the tree.
        result = []
        for key, element in self._children:
            if prefix == "" or key[:len(prefix)] == prefix:
                result.append(key)
        return set(result)
