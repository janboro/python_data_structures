#  Write a function which accepts a number and adds up all the numbers from 0 to the number passed to the fun
def sum_number_range(number):
    if number <= 0:
        return 0
    return number + sum_number_range(number - 1)


print(sum_number_range(5))
