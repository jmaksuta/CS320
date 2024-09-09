# extract values from a sorted list

import math  # optional and you can delete this line if not useful

# subroutines if any, go here

# ----------------------------------
# 60.2 Lab 2: New Words
# In this lab you will take a list of words and determine if the words are already in a word list, or are "new".

# Specifics
# You will write a routine new_words(words, wordlist) which takes two tuples of strings as arguments.
# words is an unsorted tuple of words and may contain the same word more than once.
# wordlist is a sorted tuple of words. new_words() should return a tuple of words that appear in words but are not in wordlist.

# You may assume that words and wordlist are of comparable length n.
# Your solution should run in time O(n log n).
# There are multiple possible O(n log n) solutions when you assume the two tuple lengths are comparable.
# (The list of good solutions changes if you assume the two tuple lengths are radically different).

# A few special cases to be aware of:

# If either words or wordlist or both is None, return None.
# Zero-length tuples are acceptable. (Consider this a reminder not to throw exceptions).
# If a word appears in words multiple times and is not in wordlist you can return the word once or as many times as it appears in words.
# Either result is accepted.
# if either words or wordlist is not a tuple, return None.
# If a word appears in words multiple times and is in wordlist, you must not return it in the list of new words.
# Your comparisons should be case-independent. So Able and aBLE are the same string.
# The returned tuple need not preserve case or word order.
# You may not use Python set operations.
# There's a trivial solution O(n2) solution in which you convert the tuples to sets
# and subtract wordlist from words. You may find this a useful trick for debugging,
# but [repeating] it must not appear in your solution.
# We will treat your solution as non-compliant and give you a zero (0) grade.
# Python Tips
# Python provides a built-in function sorted() which sorts a list given to it.
# To sort without regard to case, use the following incantation sorted(unsorted_list, key=str.casefold).
# You are cautioned that calling sorted() is an O(n log n) operation.

# To compare two strings in a case independent way, you can use str1.lower == str2.lower

# To discover the type of a Python object, use the type() routine. You can also use the isinstance() routine.

# Reminders
# Reminder that the code you submit must be entirely your own.
# There are several different ways to solve this problem, so don't imagine that if your code
# is the same as someone else's you can claim it is just chance.
# For details on these rules, see the syllabus.

# Also remember that beyond submitting your code, you must submit a reflection that
# discusses why you choose the particular solution you did.
# ----------------------------------

# class BinaryTree:
#   def __init__(self, root):
#     self.root = TreeNode


class TreeNode:
    def __init__(self, value=None, parent=None, left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0

    def is_external(self):
        return (self.left == None and self.right == None)

    def search(self, value, root):
        node = root
        while not node.is_external():
            if value.lower() == node.value.lower():
                break
            elif value.lower() < node.value.lower():
                node = node.left
            else:
                node = node.right
        return node

    def max(self, left_operand, right_operand):
        if (left_operand >= right_operand):
            return left_operand
        else:
            return right_operand
        
    def tallestChild(self):
        if (self.left.height >= self.right.height):
            return self.left
        else:
            return self.right
        
    def left_rotation(self, to_rotate):
        ap = to_rotate.parent
        pivot = to_rotate.right
        # t0 = to_rotate.left
        t1 = pivot.left
        # t2 = c.left
        # t3 = c.right
        pivot.parent = ap
        if pivot.value.lower() < ap.value.lower():
            ap.left = pivot
        else:
            ap.right = pivot
        # b.right = c
        # c.parent = b
        pivot.left = to_rotate
        to_rotate.parent = pivot
        # to_rotate.left = t0
        to_rotate.right = t1
        # c.left = t2
        # c.right = t3

    def right_rotation(self, to_rotate):
        # t0 = a.left
        # t1 = a.right
        pivot = to_rotate.left
        cp = to_rotate.parent
        t2 = pivot.right
        # t3 = c.right
        pivot.parent = cp
        if pivot.value.lower() < cp.value.lower():
            cp.left = pivot
        else:
            cp.right = pivot
        pivot.right = to_rotate
        to_rotate.parent = pivot
        # a.left = t0
        # a.right = t1
        to_rotate.left = t2
        # c.right = t3

        
    def restructure(self):
        # do trinode restructure on self here.
        # a = self.left
        # b = self
        # c = self.right

        # x = self
        # y = self.parent
        # z = y.parent
        
        parent = self.parent
        grand_parent = parent.parent

        if (parent.left == self and grand_parent.left == parent):
            # left subtree single rotation
            self.right_rotation(grand_parent)
        elif (parent.right == self and grand_parent.right == parent):
            # right subtree single rotation
            # left rotation
            self.left_rotation(grand_parent)
        elif (parent.left == self and grand_parent.right == parent):
            # left-right subtree double rotation
            # rotate b and c right, single rotation
            self.right_rotation(parent)
            self.left_rotation(grand_parent)
        elif (parent.right == self and grand_parent.left == parent):
            # right-left subtree double rotation
            self.left_rotation(parent)
            self.right_rotation(grand_parent)

        pass
    
    def rebalanceAVL(self, node, root):
        node.height = 1 + self.max(node.left.height, node.right.height)
        while node is not root:
            node = node.parent
            if abs(node.left.height - node.right.height) > 1:
                # Let y be the tallest child of v and let x be the tallest child of y
                y = node.tallestChild()
                x = y.tallestChild()
                # v<-restructure(x) # trinode restructure operation
                node = x.restructure()
            node.height = 1 + self.max(node.left.height, node.right.height)
        return

    # adds two external-node children to w
    def expandExternal(self):
        self.left = TreeNode(None, self)
        self.right = TreeNode(None, self)
        self.height = 1
        # This action may violate the height-balance property, however, for some nodes increase their heights by one. In particular, node,
        # and possibly some of its ancestors, increase their heights by one. Therefore, let us describe how to restructure
        # to restore its height balance.
        return self

    def add(self, value, root):
        node = self.search(value, root)
        if not node.is_external():
            return node
        if node.value == None:
            node.value = value
        else:
            # expand v into an internal node with two external node children
            node.expandExternal()
            if value.lower() < node.value.lower():
                node.left = TreeNode(value, node)
            elif value.lower() == node.value.lower():
                pass
            else:
                node.right = TreeNode(value, node)
            
            node.height = 1
            self.rebalanceAVL(node, root)
        return

    def remove(self, value, root):
        pass

   

class KeyValuePair:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

# root = TreeNode()


def load_wordlist(root, wordlist):
    for word in wordlist:
        root.add(word, root)

def internal_new_words(words, wordlist):
    root = TreeNode()
    load_wordlist(root, wordlist)
    # TODO: perform search and return result
    return None

def validate(words, wordlist):
    # TODO: write validation.
    assert words is not None
    assert wordlist is not None
    pass

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

# testing
# new_words(None, None)
# new_words(("this","that","the","other"),("this","that","a","other","walk","talk"))
