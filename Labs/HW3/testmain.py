import os
import csv
import main

def run_test_file(inputs_filename, expected_filename):
    expected_results = get_list_from_file(expected_filename)
    inputs = get_list_from_file(inputs_filename)
    
    for index in range(0, len(inputs)):
        input_list = inputs[index]
        original = list(input_list)

        actual = main.heapsort(input_list)
        # print(actual)
        expected = expected_results[index]
        check_result(index, actual, expected)
        check_result(index, original, input_list, " Original unchanged.")
        # result = lists_are_equal(actual, expected)
        # if not result:
        #     print("result at index {index} is {result}, actual={actual}, expected={expected}".format(index=index, result=result, actual=actual, expected=expected))
        # else:
        #     print("result at index {index} is {result}".format(index=index, result=result))

    # for index in range(0, len(inputs)):
    #     input_list = inputs[index]
        
    #     actual = main.heapsort(input_list)
    #     expected = None
    #     check_result(index, actual, expected)

def check_result(index, actual, expected, passed_message = ""):
    result = actual == expected
    # result = lists_are_equal(actual, expected)
    if not result:
        print("result at index {index} is {result}, actual={actual}, expected={expected}".format(index=index, result=result, actual=actual, expected=expected))
    else:
        print("result at index {index} is {result}.{passed_message}".format(index=index, result=result, passed_message=passed_message))

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


def test_args():
    result2 = main.heapsort(None)
    assert result2 == None
    print("None passes.")

    result5 = main.heapsort([])
    assert result5 == []
    print("empty list passes.")


run_test_file("inputs_data.csv", "expected_data.csv")
test_args()

