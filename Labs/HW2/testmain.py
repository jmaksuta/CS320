import os
import csv
import main

def run_test_file(inputs_filename, inputs2_filename, expected_filename):
    expected_results = get_list_from_file(expected_filename)
    inputs = get_list_from_file(inputs_filename)
    inputs2 = get_list_from_file(inputs2_filename)
    
    for index in range(0, len(inputs)):
        input_tuple = convert_to_tuple(inputs[index])
        input2_tuple = convert_to_tuple(inputs2[index])
        
        actual = main.new_words(input_tuple, input2_tuple)
        # print(actual)
        expected = convert_to_tuple(expected_results[index])
        check_result(index, actual, expected)
        # result = lists_are_equal(actual, expected)
        # if not result:
        #     print("result at index {index} is {result}, actual={actual}, expected={expected}".format(index=index, result=result, actual=actual, expected=expected))
        # else:
        #     print("result at index {index} is {result}".format(index=index, result=result))

    for index in range(0, len(inputs)):
        input_list = inputs[index]
        input2_list = inputs2[index]
        actual = main.new_words(input_list, input2_list)
        expected = None
        check_result(index, actual, expected)

def check_result(index, actual, expected):
    result = actual == expected
    # result = lists_are_equal(actual, expected)
    if not result:
        print("result at index {index} is {result}, actual={actual}, expected={expected}".format(index=index, result=result, actual=actual, expected=expected))
    else:
        print("result at index {index} is {result}".format(index=index, result=result))

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
    result = main.new_words()
    assert result == None

    result2 = main.new_words(None, ("a","b","c"))
    assert result2 == None

    result3 = main.new_words(("a","b","c"), None)
    assert result3 == None

    result3 = main.new_words(None, None)
    assert result3 == None

    result4 = main.new_words((),())
    assert result4 == ()

    result5 = main.new_words((),())
    assert result5 == ()


run_test_file("inputs1.csv", "inputs2.csv", "expected.csv")
test_args()

