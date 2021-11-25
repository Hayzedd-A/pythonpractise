def create_array(length):
    array = []
    for a in range(length):
        array.append(a + 1)
    return array


def reverse_array(array):
    out_array = []
    length = len(array)
    while length > 0:
        out_array.append(array[length-1])
        length = length-1
    return out_array


def array_to_string(array):
    string = str("")
    for a in array:
        print(a)
        string += str(a)
        string += " "
    return string


sample_array = (create_array(6))
reversed_array = reverse_array(sample_array)
print(array_to_string(reversed_array))
