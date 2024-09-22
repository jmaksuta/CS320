import math # optional and you can delete this line if not useful

# subroutines if any, go here
class KeyPair:
    def __init__(self, key: int=None, element=None, left_tree=None, right_tree=None) -> None:
        self.key = key
        self.element = element

    def is_internal(self):
        return self.left_tree == None and self.right_tree == None


    # def swap(self, list, up_elem_index, down_elem_index):
    #     temp = list[up_elem_index]
    #     list[up_elem_index] = list[down_elem_index]
    #     list[down_elem_index] = temp
    #     return
        

    # def insert(self, heap_node = None, list : list = None)->None:
    #     # n = n + 1
    #     # list[n] = heap_node
    #     list.append(heap_node)
        
    #     i = len(list)
    #     while i > 1 and list[int(i / 2)] > list[i]:
    #         self.swap(list[int(i / 2)], list[i])
    #         i = int(i / 2)
    #     return
    

    # def remove_min(self, list):
    #     temp = list[1]
    #     n = len(list)
    #     list[1] = list[n]
    #     n = n - 1
    #     i = 1
    #     while i < n:
    #         if ((2 * i) + 1) <= n:
    #             if (list[i] <= list[2 * i] and list[i] <= list[(2 * i) + 1]):
    #                 return temp
    #             else:
    #                 j = math.min(list[2 * i], list[(2 * i)+1])
    #                 self.swap(list[i], list[j])
    #                 i = j
    #         else:
    #             if (2 * i) <= n:
    #                 if (list[i] > list[2 * i]):
    #                     self.swap(list[i], list[j])
    #             return temp
    #     return temp                
    
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
    def is_less(self, a, b)->bool:
        return a < b
    # isLessOrEqualTo : True if and only if is less than or equal to .
    def is_less_or_equal_to(self, a, b)->bool:
        return a <= b
    # isEqualTo : True if and only if and are equal.
    def is_equal_to(self, a, b)->bool:
        return a == b
    # isGreater : True if and only if is greater than .
    def is_greater(self, a, b)->bool:
        return a > b

    # isGreaterOrEqualTo : True if and only if is greater than or equal to .
    def is_greater_or_equal_to(self, a, b)->bool:
        return a >= b
    # isComparable : True if and only if can be compared.
    def is_comparable(self, a, b)->bool:
        pass



class Heap:
    def __init__(self, root:KeyPair=None, comparator=None) -> None:
        self.root = root
        self.last_node = root
        self.comparator = comparator
        self.list = []

    # def insert(self, heap_node:KeyPair):
    #     if self.root == None:
    #         self.root = heap_node
    #     else:
    #         self.root.insert(heap_node, self.list)
    #     return

    

    def swap(self, up_elem_index, down_elem_index):
        temp = self.list[up_elem_index]
        self.list[up_elem_index] = self.list[down_elem_index]
        self.list[down_elem_index] = temp
        return


    def greater_than(self, left_operand, right_operand):
        return left_operand > right_operand


    def insert(self, element = None)->None:
        # n = n + 1
        # list[n] = element
        self.list.append(element)
        
        current = len(self.list)
        while current > 1 and self.greater_than(self.nth_elem(int(current / 2)), self.nth_elem(current)):
            # self.list[int(last_index / 2)].element > self.list[last_index].element:
            parent_index = int((current - 1) / 2)
            child_index = (current - 1)
            self.swap(parent_index, child_index)
            current = int(current / 2)
        return
    

    def nth_of_smaller(self, nth_elem_a, nth_elem_b):
        result = None
        if self.nth_elem(nth_elem_a) <= self.nth_elem(nth_elem_b):
            result = nth_elem_a
        else:
            result = nth_elem_b
        return result

    def to_index(self, value):
        return value - 1
    
    def nth_elem(self, n):
        return self.list[self.to_index(n)]

    def remove_min(self):
        temp = self.list[0]
        n = len(self.list)
        self.list[0] = self.nth_elem(n)
        n = n - 1
        i = 1
        while i < n:
            if ((2 * i) + 1) <= n:
                if (self.nth_elem(i) <= self.nth_elem(2 * i) and self.nth_elem(i) <= self.nth_elem((2 * i) + 1)):
                    return temp
                else:
                    j = self.nth_of_smaller(2 * i, (2 * i) + 1)
                    # j = math.min(self.list[(2 * i) - 1], self.list[((2 * i) + 1) - 1])
                    self.swap(self.to_index(i), self.to_index(j))
                    i = j
            else:
                if (2 * i) <= n:
                    if (self.nth_elem(i) > self.nth_elem(2 * i)):
                        self.swap(self.to_index(i), self.to_index(2 * i))
                return temp
        return temp           



def internal_heapsort(hlist):
    result = []
    the_heap = Heap()
    for index in range(0, len(hlist)):
        input_value = hlist[index]
        the_heap.insert(input_value)

    # Todo create a list from the elements

    for index in range(len(the_heap.list)):
        result.append(the_heap.remove_min())

    return result


# validates the input arguments
def validate(hlist):
    hlist_not_none = hlist is not None
    passed = hlist_not_none
    return passed


# fill in heapsort
def heapsort(hlist):
    result = None
    if validate(hlist):
        working_copy = list(hlist)
        result = internal_heapsort(working_copy)
    return result
