def product_of_array(array):
    if len(array) == 0:
        return 1
    return array.pop() * product_of_array(array)


print(product_of_array([1, 2, 3, 10]))
