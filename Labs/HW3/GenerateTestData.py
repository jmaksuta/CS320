import random

random.seed(10)


def get_test_list_data():
    result = []
    random.seed(random.randint(1, 1000))

    data_length = random.randint(1,100)
    for index in range(0, data_length):
        result.append(random.randint(0,9999999))
    return result

def generate_test_data(file_name, number_of_elements):
    lists = []
    for index in range(0, number_of_elements):
        lists.append(get_test_list_data())
    
    inputs = []
    expecteds = []
    for index in range(0, len(lists)):
        input = lists[index]
        expected = sorted(list(lists[index]))
        inputs.append((str(input).replace("[","").replace("]","").replace(" ","") + "\n"))
        expecteds.append(str(expected).replace("[","").replace("]","").replace(" ","") + "\n")

    inputs_filename = "{prefix}{filename}".format(prefix="inputs_",filename=file_name)
    inputs_file = open(inputs_filename, "w")
    inputs_file.writelines(inputs)
    inputs_file.close()

    outputs_filename = "{prefix}{filename}".format(prefix="expected_",filename=file_name)
    outputs_file = open(outputs_filename, "w")
    outputs_file.writelines(expecteds)
    outputs_file.close()

generate_test_data("data.csv", 10)