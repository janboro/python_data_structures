def flattern_array(array):
    if array[0] is type(list):
        return flattern_array(array[0])
