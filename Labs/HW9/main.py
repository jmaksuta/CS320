"""
Lab 09 - HW9
67.2 Implementing a Trie
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""


class Trie:
    def __init__(self, is_word):
        self.is_word = False  # notes if this node is, itself, a word as well as a possible prefix
        self._children = {}  # children are a dictionary

    def add(self, key: str) -> bool:
        """ Adds a string to the trie.
        Returns True if the key was not already in the trie and
        False if the key is a duplicate or was None or the empty string. """
        result = False
        if key is None or len(key) == 0 or self.find(key):
            return False
        index = 0
        character = key[index]
        result = character in self._children
        if not result:
            self._children[character] = Trie()
            result = True
        next = key[index + 1:]
        if len(next) > 0:
            result = (result and self._children[character].add(next))
        else:
            self._children[character].is_word = True
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
        return result

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
        return result

    def partial(self, prefix: str) -> set[str]:
        """ Returns a set of all words that begin with the string in prefix.
        Returns an empty set if the prefix is not present or the prefix is None. """
        if prefix is None or (not self.find(prefix) and len(prefix) > 0):
            return set()
        elif len(prefix) == 0:
            return self._get_all_words(prefix)
        return self._partial(prefix, "")
    
    def _partial(self, prefix: str, word) -> set[str]:
        result = set()
        index = 0
        character = prefix[index]
        if character in self._children:
            word += character
            next = prefix[index + 1:]
            if len(next) == 0:
                # traverse down and get the words
                words = []
                for key, value in self._children[character]._children.items():
                    if value.is_word:
                        words.append(word + key)
                    words += value._get_words(key, word + key)
                for value in words:
                    result.add(value)
            else:
                result = result.union(self._children[character]._partial(next, word))
        return result
    
    def _get_all_words(self, word):
        result = set()
        words = []
        for key, value in self._children.items():
            if value.is_word:
                words.append(word + key)
            words += value._get_words(key, word + key)
        for value in words:
            result.add(value)
        return result
    
    def _get_words(self, character, word):
        result = []
        for key, value in self._children.items():
            if value.is_word:
                result.append(word + key)
            result += value._get_words(key, word + key)
        return result
