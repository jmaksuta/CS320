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

def get_expected_result_from_file(file_name, graph: GraphEL):
    result = [None,None]
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        row_index = 0
        for row in reader:
            result[row_index] = []
            vertices = tuple(row)
            if len(vertices) > 0:
                index = 0
                current = vertices[index]
                while current is not None:
                    index += 1
                    if index < len(vertices):
                        vertex = vertices[index]
                        edge = graph.get_edge_with_ends(VertexEL(current), VertexEL(vertex))
                        if edge is not None:
                            result[row_index].append(edge)
                        current = vertex
                    else:
                        current = None
            # result[row_index] = tuple(row)
            result[row_index] = tuple(result[row_index])
            row_index += 1

    return tuple(result)

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

def test_args():
    # If graph is None, return an empty tuple (())
    # If start is None, return an empty tuple (())
    # If start is not in graph, return an empty tuple(())
    test_multiway_1()
    test_graph_3()
    test_doubleton_2()
    test_simple_graph2()
    test_doubleton()
    test_graph_files()
    test_none_value_args()
    test_vertex_in_graph()


def test_none_value_args():
    result = main.bellman_ford(None, None, None)
    assert result == (None, None)
    print("None graph, None start, and None end passes.")

    result = main.bellman_ford(None, None, VertexEL("Test"))
    assert result == (None, None)
    print("None graph and None start passes.")

    result = main.bellman_ford(None, VertexEL("Test"), None)
    assert result == (None, None)
    print("None graph and None end passes.")

    test_graph = GraphEL()

    result = main.bellman_ford(test_graph, None, None)
    assert result == (None, None)
    print("test_graph, None start, and None end passes.")

    result = main.bellman_ford(test_graph, None, VertexEL("Test"))
    assert result == (None, None)
    print("test_graph and None start passes.")

    result = main.bellman_ford(test_graph, VertexEL("Test"), None)
    assert result == (None, None)
    print("test_graph and None end passes.")


def test_vertex_in_graph():    
    empty_graph = GraphEL()
    start = VertexEL("A")
    end = VertexEL("Z")
    result = main.bellman_ford(empty_graph, start, end)
    assert result == (None, None)
    print("start and end not in empty graph passes.")

    start_a = VertexEL("A")
    end_a = VertexEL("Z")
    graph_a = GraphEL()
    graph_a.add_vertex(start_a)
    result = main.bellman_ford(graph_a, start_a, end_a)
    assert result == (None, None)
    print("end not in graph passes.")

    start_b = VertexEL("A")
    end_b = VertexEL("Z")
    graph_b = GraphEL()
    graph_b.add_vertex(end_b)
    result = main.bellman_ford(graph_b, start_b, end_b)
    assert result == (None, None)
    print("start not in graph passes.")

    start_c = VertexEL("'A'")
    end_c = VertexEL("'Z'")
    graph_c = GraphEL()
    graph_c.add_vertex(start_c)
    graph_c.add_vertex(end_c)
    result = main.bellman_ford(graph_c, start_c, end_c)
    # assert result != (None, None)
    # print("start and end in graph passes.")

def test_graph_files():
    dir_list = os.listdir("./Graph_Files")
    print(dir_list)

    for file in sorted(dir_list):
        try:
            graph_filename = "./Graph_Files/{file}".format(file=file)
            graph = parse_graph_file(graph_filename)
            expected = get_expected_result_from_file("./Expected_Results/{file}".format(file=file), graph)
            
            args = get_row_from_csv_file(graph_filename, 0)
            v1 = VertexEL(args[0])
            v2 = VertexEL(args[1])
            actual = main.bellman_ford(graph, v1, v2)

            print("Testing {file}.".format(file=file), end='')
            test_expected_and_actual(expected, actual)
        except Exception as e:
            print(e)
            print(" Failed.")


def test_doubleton():
    try:
        graph_filename = "./IndividualTests/Doubleton.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        expected = ((graph.get_edge_with_ends(v1, v2),), (graph.get_edge_with_ends(v2, v1),))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert expected == actual
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")


def test_doubleton_2():
    try:
        graph_filename = "./IndividualTests/Doubleton2.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BC = graph.get_edge_with_ends(VertexEL("B"), VertexEL("C"))
        CD = graph.get_edge_with_ends(VertexEL("C"), VertexEL("D"))

        DC = graph.get_edge_with_ends(VertexEL("D"), VertexEL("C"))
        CB = graph.get_edge_with_ends(VertexEL("C"), VertexEL("B"))
        BA = graph.get_edge_with_ends(VertexEL("B"), VertexEL("A"))

        shortest_path = ((AB,BC,CD),(DC,CB,BA))

        assert (actual == shortest_path)

        
        AE = graph.get_edge_with_ends(VertexEL("A"), VertexEL("E"))
        BF = graph.get_edge_with_ends(VertexEL("B"), VertexEL("F"))
        CG = graph.get_edge_with_ends(VertexEL("C"), VertexEL("G"))

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BD = graph.get_edge_with_ends(VertexEL("B"), VertexEL("D"))
        DE = graph.get_edge_with_ends(VertexEL("D"), VertexEL("E"))
        EF = graph.get_edge_with_ends(VertexEL("E"), VertexEL("F"))
        FC = graph.get_edge_with_ends(VertexEL("F"), VertexEL("C"))
        CA = graph.get_edge_with_ends(VertexEL("C"), VertexEL("A"))
        expected = ((AB, BD, DE, EF), (FC, CA))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert expected == actual
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")
        

def test_graph_3():
    try:
        graph_filename = "./Graph_Files/graph003.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BC = graph.get_edge_with_ends(VertexEL("B"), VertexEL("C"))
        CD = graph.get_edge_with_ends(VertexEL("C"), VertexEL("D"))

        DC = graph.get_edge_with_ends(VertexEL("D"), VertexEL("C"))
        CB = graph.get_edge_with_ends(VertexEL("C"), VertexEL("B"))
        BA = graph.get_edge_with_ends(VertexEL("B"), VertexEL("A"))

        shortest_path = ((AB,BC,CD),(DC,CB,BA))

        assert (actual == shortest_path)

        
        AE = graph.get_edge_with_ends(VertexEL("A"), VertexEL("E"))
        BF = graph.get_edge_with_ends(VertexEL("B"), VertexEL("F"))
        CG = graph.get_edge_with_ends(VertexEL("C"), VertexEL("G"))

        BD = graph.get_edge_with_ends(VertexEL("B"), VertexEL("D"))
        DE = graph.get_edge_with_ends(VertexEL("D"), VertexEL("E"))
        EF = graph.get_edge_with_ends(VertexEL("E"), VertexEL("F"))
        FC = graph.get_edge_with_ends(VertexEL("F"), VertexEL("C"))
        CA = graph.get_edge_with_ends(VertexEL("C"), VertexEL("A"))

        expected = ((AB, BD, DE, EF), (FC, CA))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert expected == actual
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")


def test_multiway_1():
    try:
        graph_filename = "./IndividualTests/Multiway1.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BD = graph.get_edge_with_ends(VertexEL("B"), VertexEL("D"))
        DE = graph.get_edge_with_ends(VertexEL("D"), VertexEL("E"))
        EB = graph.get_edge_with_ends(VertexEL("E"), VertexEL("B"))
        BA = graph.get_edge_with_ends(VertexEL("B"), VertexEL("A"))

        expected = ((AB, DE),(DE, EB, BA))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert compare_results(expected, actual)
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")

def compare_results(expected, actual):
    # compare index 0
    index0_passed = test_index(expected, actual, 0)
    # compare index 1
    index1_passed = test_index(expected, actual, 1)
    return index0_passed and index1_passed

def test_index(expected, actual, ind):
    try:
        index1_passsed = False
        if expected[ind] is None:
            if actual[ind] is None:
                index1_passsed = True
            else:
                index1_passsed = False
        else:
            for index in range(0, len(expected[ind])):
                if str(expected[ind][index]) != str(actual[ind][index]):
                    index1_passsed = False
                    break  
    except Exception as e:
        index1_passsed = False

    return index1_passsed

def test_simple_graph():
    try:
        graph_filename = "./IndividualTests/SimpleGraph.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BD = graph.get_edge_with_ends(VertexEL("B"), VertexEL("D"))
        expected = ((AB,BD), (graph.get_edge_with_ends(v2, v1),))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert expected == actual
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")

def test_simple_graph2():
    try:
        graph_filename = "./IndividualTests/SimpleGraph2.csv"
        graph = parse_graph_file(graph_filename)
        args = get_row_from_csv_file(graph_filename, 0)
        v1 = VertexEL(args[0])
        v2 = VertexEL(args[1])
        actual = main.bellman_ford(graph, v1, v2)

        AB = graph.get_edge_with_ends(VertexEL("A"), VertexEL("B"))
        BD = graph.get_edge_with_ends(VertexEL("B"), VertexEL("D"))
        DE = graph.get_edge_with_ends(VertexEL("D"), VertexEL("E"))
        EF = graph.get_edge_with_ends(VertexEL("E"), VertexEL("F"))
        FC = graph.get_edge_with_ends(VertexEL("F"), VertexEL("C"))
        CA = graph.get_edge_with_ends(VertexEL("C"), VertexEL("A"))

        expected = ((AB, BD, DE, EF), (FC, CA))

        print("Testing {file}.".format(file=graph_filename))
        print(f"expected={expected},\nactual={actual}")
        print("Testing {file}.".format(file=graph_filename), end='')
        assert expected == actual
        print(" Passed.")
        # test_expected_and_actual(expected, actual)
    except Exception as e:
        print(e)
        print(" Failed.")


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
        print(" Failed. expected={expected}, acutal={actual}".format(expected=expected, actual=actual))
    # graph1 = GraphEL()

    # testV1 = VertexEL("Test")

    # result = main.bellman_ford(graph1, testV1)
    # assert result == (())
    # print("None start passes.")


VALUE_INDEX = 2

# def print_values(item_list):
#     for index in range(0, len(item_list)):
#         print(item_list[index][VALUE_INDEX], end=", ")
#     print("")

# print(main.bellman_ford(3, make_fields(6, 0)))
# print(main.bellman_ford(20, make_fields(20, 0)))
# print(main.bellman_ford(20, make_full_fields(20)))
# print(main.bellman_ford(45, (())))

test_args()

