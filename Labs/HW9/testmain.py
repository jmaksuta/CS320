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
    run_test("add_keys None", test_add_keys_none)
    run_test("add_keys empty", test_add_keys_empty)
    run_test("add_keys duplicate", test_add_keys_duplicate)
    run_test("add keys with a None value", test_add_keys_with_a_none)
    run_test("add keys with smaller", test_add_keys_with_smaller)
    

def test_add_keys_none():
    keys = None
    trie_a = Trie()
    result = trie_a.add_keys(keys)
    assert result == 0

def test_add_keys_empty():
    keys = ()
    trie_a = Trie()
    result = trie_a.add_keys(keys)
    assert result == 0

def test_add_keys_duplicate():
    keys = ("test","test")
    trie_a = Trie()
    result = trie_a.add_keys(keys)
    assert result == 1

def test_add_keys_with_a_none():
    keys = ("test","tester", None,"best")
    trie_a = Trie()
    result = trie_a.add_keys(keys)
    assert result == 3

def test_add_keys_with_smaller():
    keys = ("test","tes", None,"best")
    trie_a = Trie()
    result = trie_a.add_keys(keys)
    assert result == 2


def test_remove():
    run_test("remove None", test_remove_none)
    run_test("remove empty", test_remove_empty)
    run_test("remove not found", test_remove_not_found)
    run_test("remove key", test_remove_key)

def test_remove_none():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.remove(None)
    assert result == False

def test_remove_empty():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.remove("")
    assert result == False

def test_remove_not_found():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.remove("a")
    assert result == False

def test_remove_key():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.remove(keys[0])
    assert result == True

def test_find():
    run_test("find None", test_find_none)
    run_test("find empty", test_find_empty)
    run_test("find exists", test_find_exists)
    run_test("find not exists", test_find_not_exists)

def test_find_none():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.find(None)
    assert result == False

def test_find_empty():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.find("")
    assert result == False

def test_find_exists():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.find("test")
    assert result == False

def test_find_not_exists():
    keys = ("test")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.find("tester")
    assert result == False

def test_partial():
    run_test("partial none", test_partial_none)
    run_test("partial empty", test_partial_empty)
    run_test("partial not found", test_partial_not_found)
    run_test("partial found", test_partial_found)

def test_partial_none():
    keys = ("test","tester","lester","onion","tesla","apple","orange")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.partial(None)
    assert len(result) == 0

def test_partial_empty():
    keys = ("test","tester","lester","onion","tesla","apple","orange")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.partial("")
    assert len(result) == len(keys)

def test_partial_not_found():
    keys = ("test","tester","lester","onion","tesla","apple","orange")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.partial("and")
    assert len(result) == 0

def test_partial_found():
    keys = ("test","tester","lester","onion","tesla","apple","orange")
    trie_a = Trie()
    count = trie_a.add_keys(keys)
    result = trie_a.partial("tes")
    assert len(result) == 3


def run_test(test_name, test):
    try:
        test()
        print("Test {test_name} passes.".format(test_name=test_name))
    except AssertionError as e:
        print("Test {test_name} failed, {error}".format(test_name=test_name, error=e))

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

