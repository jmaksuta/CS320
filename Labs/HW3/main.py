import math # optional and you can delete this line if not useful

class HeapNode:
    def __init__(self, key=None, element=None, left_tree=None, right_tree=None) -> None:
        self.key = key
        self.element = element
        self.left_tree = left_tree
        self.right_tree = right_tree


    def is_internal(self):
        return self.left_tree == None and self.right_tree == None

    def swap(list, up_elem_index, down_elem_index):
        # temp = up_elem
        pass
        
    def insert(self, heap_node: HeapNode, list)->None:
        n = n + 1
        list[n] = heap_node
        i = n
        while i > 1 and list[int(i/2)] > list[i]:
            self.swap(list[int(i/2)], list[i])
            i = int(i / 2)
        return
    

    def remove_min(self, list):
        temp = list[1]
        list[1] = list[n]
        n = n - 1
        i = 1
        while i < n:
            if ((2*i) + 1) <= n:
                if (list[i] <= list[2*i] and list[i] <= list[(2*i) + 1]):
                    return temp
                else:
                    j = math.min(list[2*i], list[(2*i)+1])
                    self.swap(list[i], list[j])
                    i = j
            else:
                if (2*i) <= n:
                    if (list[i] > list[2*i]):
                        self.swap(list[i], list[j])
                return temp
        return temp                
    
    def level_number():
        # Level numbering the nodes of a binary tree
        # For every node of , let be the integer defi ned as follows:
        # If v is the root of T, the p(v) = 1
        # If v is the left child of node u, then p(v) = 2p(u)
        # If v is the right child of node u, then p(v) = 2p(u) + 1
        pass


class Comparator:
    def __init__(self) -> None:
        return
    
    def compare(operand_a, operand_b):
        result = 0
        if operand_a > operand_b:
            result = 1
        elif (operand_a == operand_b):
            result = 0
        else:
            result = -1
        return result
    
    # isLess : True if and only if is less than .
    def is_less(a, b)->type:
        return type(True)
    # isLessOrEqualTo : True if and only if is less than or equal to .
    # isEqualTo : True if and only if and are equal.
    # isGreater : True if and only if is greater than .
    # isGreaterOrEqualTo : True if and only if is greater than or equal to .
    # isComparable : True if and only if can be compared.



class Heap:
    def __init__(self, root:HeapNode=None, comparator=None) -> None:
        self.root = root
        self.last_node = root
        self.comparator = comparator
        self.list = []

    def insert(self, heap_node:HeapNode):
        if self.root == None:
            self.root = heap_node
        else:
            self.root.insert(heap_node, self.list)
        return

    def BottomUpHeap(S):
        pass


# subroutines if any, go here
def internal_heapsort(hlist):
    result = []
    the_heap = Heap()
    for index in range(0, len(hlist)):
        input_value = hlist[index]
        the_heap.insert(HeapNode(input_value, input_value))

    return result


# validates the input arguments
def validate(hlist):
    hlist_not_none = hlist is not None
    passed = hlist_not_none
    return passed

# fill in heapsort
def heapsort(hlist):
    result = None
    compare = Comparator()
    compare.is_less(1, 2)
    
    if validate(hlist):
        result = internal_heapsort(hlist)
    return result