import os
import csv
import main
import trie_test
from main import Trie
import time

def run_test_file(inputs_filename, expected_filename):
    expected_results = get_list_from_file(expected_filename)
    inputs = get_list_from_file(inputs_filename)
    elapsed_times = []
    total_elapsed = 0

    for index in range(0, len(inputs)):
        input_list = inputs[index]
        original = list(input_list)

        start_time = time.time()

        # actual = main.bellman_ford(convert_to_int_list(input_list))

        end_time = time.time()

        actual = convert_to_str_list(actual)
        # print(actual)
        expected = expected_results[index]
        check_result(index, actual, expected)
        check_result(index, original, input_list, " Original unchanged.")
        elapsed = end_time - start_time
        print("Elapsed Time: {time:.6}".format(time=elapsed))
        elapsed_times.append(elapsed)
        total_elapsed += elapsed
    
    average_time = total_elapsed / len(elapsed_times)
    print("Average Time: {avg:.6}".format(avg=average_time))

def check_result(index, actual, expected, passed_message = ""):
    result = actual == expected
    # result = lists_are_equal(actual, expected)
    if not result:
        print("result at index {index} is {result}, actual={actual}, expected={expected}".format(index=index, result=result, actual=actual, expected=expected))
    else:
        print("result at index {index} is {result}.{passed_message}".format(index=index, result=result, passed_message=passed_message))

def convert_to_int_list(the_list):
    result = []
    for index in range(0, len(the_list)):
        result.append(int(the_list[index]))
    return result

def convert_to_str_list(the_list):
    result = []
    for index in range(0, len(the_list)):
        result.append(str(the_list[index]))
    return result

def convert_to_tuple(the_list):
    result = None
    if the_list != None:
        result = tuple(the_list)
    return result

def lists_are_equal(actual, expected):
    result = True
    if len(actual) == len(expected):
        for n in range(0, len(actual)):
            if actual[n] != expected[n]:
                result = False
                break
    else:
        result = False
    return result


def get_list_from_file(file_name):
    result = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            if len(row) == 0:
                result.append([])
            elif row[0] == "None":
                result.append(None)
            else:
                result.append(row)

    return result

def get_row_from_csv_file(file_name, index):
    result = None
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        row_index = 0
        for row in reader:
            if row_index == index:
                result = row
                break
            row_index += 1

    return result

def make_fields(length, num_obstacles):
    field = ((True,) * length,) * length
    return field

def make_full_fields(length):
    field = ((False,) * length,) * length
    return field

def run_tests():
    # If graph is None, return an empty tuple (())
    # If start is None, return an empty tuple (())
    # If start is not in graph, return an empty tuple(())
    test_none_value_args()
    test_add()
    test_add_keys()
    test_remove()
    test_find()
    test_partial()


def test_none_value_args():
    pass


def test_add():
    test_add_none()
    test_add_empty()
    test_add_duplicate()


def test_add_none():
    test_name = "add None"
    try:
        trie_a = Trie()
        test_value = None
        resultA = trie_a.add(test_value)
        assert resultA == False
        print("Test {test_name} passes.".format(test_name=test_name))
    except AssertionError as e:
        print("Test {test_name} failed, {error}".format(test_name=test_name, error=e))


def test_add_empty():
    test_name = "add empty"
    try:
        trie_a = Trie()
        test_value = ""
        resultA = trie_a.add(test_value)
        assert resultA == False
        print("Test {test_name} passes.".format(test_name=test_name))
    except AssertionError as e:
        print("Test {test_name} failed, {error}".format(test_name=test_name, error=e))


def test_add_duplicate():
    test_name = "add duplicate"
    try:
        trie_a = Trie()
        test_value = "test"
        resultA = trie_a.add(test_value)
        resultB = trie_a.add(test_value)
        assert resultA == True and resultB == False
        print("Test {test_name} passes.".format(test_name=test_name))
    except AssertionError as e:
        print("Test {test_name} failed, {error}".format(test_name=test_name, error=e))


def test_add_keys():
    pass


def test_remove():
    pass


def test_find():
    pass


def test_partial():
    pass

# def test_graph_files():
#     dir_list = os.listdir("./Graph_Files")
#     print(dir_list)

#     for file in sorted(dir_list):
#         try:
#             graph_filename = "./Graph_Files/{file}".format(file=file)
#             graph = parse_graph_file(graph_filename)
#             expected = get_expected_result_from_file("./Expected_Results/{file}".format(file=file), graph)
            
#             args = get_row_from_csv_file(graph_filename, 0)
#             v1 = VertexEL(args[0])
#             v2 = VertexEL(args[1])
#             actual = main.bellman_ford(graph, v1, v2)

#             print("Testing {file}.".format(file=file), end='')
#             test_expected_and_actual(expected, actual)
#         except Exception as e:
#             print(e)
#             print(" Failed.")


VALUE_INDEX = 2

run_tests()

