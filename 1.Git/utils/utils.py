def sum_2d_array(array_2d):
    sum_of_array = 0

    for array in array_2d:
        for element in array:
            sum_of_array += element

    return sum_of_array


def sum_1d_array(array):
    return sum(array)