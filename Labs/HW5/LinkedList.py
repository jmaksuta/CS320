"""
LinkedList and Node
Written By John Maksuta
CS320-801 Fall 2024
Dr. Partridge
"""

class Node:
    ''' A node in the linked list. '''
    def __init__(self, value) -> None:
        self.previous = None
        self.value = value
        self.next = None

class LinkedList:
    ''' A linked list. '''
    def __init__(self) -> None:
        self.last = None
        self.first = None
        self.length = 0

    def first(self):
        return self.first
    
    def last(self):
        return self.last
    
    def length(self):
        return self.length

    def append(self, value):
        if self.first is None:
            node = Node(value)
            self.last = node
            self.first = node
            node.previous = node
            node.next = node
            self.length += 1
        else:
            node = self.insertAfter(self.last, value)
            if node is not None:
                self.length += 1
            
    def insertAfter(self, parent, value):
        node = Node(value)
        # node.value = value
        node.previous = parent
        node.next = parent.next
        parent.next.previous = node
        parent.next = node
        self.last = node
        return node
    
    def remove(self, node):
        temp = node.value
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = None
        node.next = None
        return temp
    
    def pop(self):
        value = None
        value = self.remove(self.last)
        if value is not None:
            self.length -= 1
    
    def print_all(self):
        output = ""
        current = self.first
        output += "{value}".format(value=current.value)
        current = current.next
        while current is not self.last.next:
            output += ",{value}".format(value=current.value)
            current = current.next
        print(output)