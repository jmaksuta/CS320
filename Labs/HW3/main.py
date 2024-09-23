# import math # optional and you can delete this line if not useful

# subroutines if any, go here

class Heap:
    def __init__(self, root=None, comparator=None) -> None:
        self.root = root
        self.last_node = root
        self.comparator = comparator
        self.list = []

    def swap(self, up_elem_index, down_elem_index):
        temp = self.list[up_elem_index]
        self.list[up_elem_index] = self.list[down_elem_index]
        self.list[down_elem_index] = temp
        return

    def to_index(self, value):
        return value - 1
    
    def nth_elem(self, n):
        return self.list[self.to_index(n)]

    def greater_than(self, left_operand, right_operand):
        return left_operand > right_operand
    
    def less_than(self, left_operand, right_operand):
        return left_operand > right_operand

    def insert(self, element=None) -> None:
        # n = n + 1
        # A[n] <- (k,e)
        self.list.append(element)
        # i <- n
        current_index = len(self.list) - 1
        # while i > 1 and A[floor(1/2)] > A[i] do
        while current_index > 0 and self.greater_than(self.list[int((current_index - 1) / 2)],
                                                      self.list[current_index]):
            # self.list[int(last_index / 2)].element > self.list[last_index].element:
            # Swap A[floor(i/2)] and A[i]
            parent_index = int((current_index - 1) / 2)
            child_index = current_index
            self.swap(parent_index, child_index)
            # i <- floor(i/2)
            current_index = parent_index
        return
    
    def nth_of_smaller(self, nth_elem_a, nth_elem_b):
        result = None
        if self.nth_elem(nth_elem_a) <= self.nth_elem(nth_elem_b):
            result = nth_elem_a
        else:
            result = nth_elem_b
        return result
    
    def index_of_smaller(self, index_a, index_b):
        result = -1
        if self.list[index_a] <= self.list[index_b]:
            result = index_a
        else:
            result = index_b

        return result

    def remove_min(self):
        # temp <- A[1]
        temp = self.list[0]
        n = len(self.list)
        # A[1] <- A[n]
        # self.list.remove(self.nth_elem(n))
        self.list[0] = self.nth_elem(n)
        # n <- n - 1
        n = n - 1
        self.list = self.list[:n]
        # i <- 1
        current_index = 0
        # while i < n do
        while current_index < n:
            
            index_a = (2 * current_index) + 1
            index_b = (2 * current_index) + 2
            # if 2i + 1 <= n then # node has 2 internal children
            if index_b < n:
                # if A[i] <= A[2i] and A[i] <= A[2i + 1] then
                current_less_than_child_a = self.list[current_index] <= self.list[index_a]
                current_less_than_child_b = self.list[current_index] <= self.list[index_b]
                if current_less_than_child_a and current_less_than_child_b:
                    # return temp # we have restored the heap-order property
                    return temp
                # else
                else:
                    # Let j be the index of the smaller of A[2i] and A[2i + 1]
                    smaller_index = self.index_of_smaller(index_a, index_b)
                    # j = math.min(self.list[(2 * i) - 1], self.list[((2 * i) + 1) - 1])
                    # Swap A[i] and A[j]
                    self.swap(current_index, smaller_index)
                    # i <- j
                    current_index = smaller_index
            # else # this node has zero or one internal child
            else:
                # if 2i <= n then # this node has one internal child (th last node)
                if index_a < n:
                    # if A[i] > A[2i]
                    if self.list[current_index] > self.list[index_a]:
                        # Swap A[i] and A[2i]
                        self.swap(current_index, index_a)
                # return temp # we have restored the heap-order property
                return temp
        # return temp # we reached the last node or an external node
        
        return temp           


def internal_heapsort(hlist):
    result = []
    the_heap = Heap()
    for index in range(0, len(hlist)):
        input_value = int(hlist[index])
        the_heap.insert(input_value)

    for index in range(len(the_heap.list)):
        result.append(str(the_heap.remove_min()))
        # print("DEBUG: list={value}".format(value=the_heap.list))

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
