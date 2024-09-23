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