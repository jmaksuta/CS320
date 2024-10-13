import os
import csv
import main
from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file
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

        # actual = main.dfs(convert_to_int_list(input_list))

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

def make_fields(length, num_obstacles):
    field = ((True,) * length,) * length
    return field

def make_full_fields(length):
    field = ((False,) * length,) * length
    return field

def test_args():
    # If graph is None, return an empty tuple (())
    # If start is None, return an empty tuple (())
    # If start is not in graph, return an empty tuple(())
    result = main.dfs(None, None)
    assert result == (())
    print("None graph and None start passes.")

    result = main.dfs(None, VertexEL("Test"))
    assert result == (())
    print("None graph passes.")

    graph1 = GraphEL()
    result = main.dfs(graph1, None)
    assert result == (())
    print("None start passes.")

    test_vertex_in_graph()
    test_graph_files()


def test_vertex_in_graph():    
    graph1 = GraphEL()
    testV1 = VertexEL("Test")

    result = main.dfs(graph1, testV1)
    assert result == (())
    print("Vertex in graph passes.")

def test_graph_files():
    dir_list = os.listdir("./Graph_Files")
    print(dir_list)
    

    for file in dir_list:
        expected = get_list_from_file("./Expected_Results/{file}".format(file=file))
        
        graph = parse_graph_file("./Graph_Files/{file}".format(file=file))
        v1 = graph.vertices()[0]
        actual = main.dfs(graph, v1)

        print("Testing {file}.".format(file=file), end='')
        test_expected_and_actual(expected, actual)


def list_to_vertex_tuple(list):
    result = []
    for elem in list:
        result.append(VertexEL(elem))
    return tuple(result)

def test_expected_and_actual(expected, actual):
    try:
        is_passed = False
        for value in expected:
            if list_to_vertex_tuple(value) == actual:
                is_passed = True
                break
        assert is_passed == True
        print(" Passed.")
    except Exception as e:
        print(" Failed.")
    # graph1 = GraphEL()

    # testV1 = VertexEL("Test")

    # result = main.dfs(graph1, testV1)
    # assert result == (())
    # print("None start passes.")


VALUE_INDEX = 2

# def print_values(item_list):
#     for index in range(0, len(item_list)):
#         print(item_list[index][VALUE_INDEX], end=", ")
#     print("")

# print(main.dfs(3, make_fields(6, 0)))
# print(main.dfs(20, make_fields(20, 0)))
# print(main.dfs(20, make_full_fields(20)))
# print(main.dfs(45, (())))

test_args()

