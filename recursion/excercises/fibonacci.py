def fibonacci(fibonacci_nth_number):
    if fibonacci_nth_number < 2:
        return fibonacci_nth_number
    return fibonacci(fibonacci_nth_number - 1) + fibonacci(fibonacci_nth_number - 2)


print(fibonacci(35))
