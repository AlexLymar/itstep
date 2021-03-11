def only_odd_arguments(func):
    def wrapper(*args):
        for i in func(*args):
            if i % 2:
                return func
            else:
                print('Please add odd numbers!')
    return wrapper

@only_odd_arguments
def add(a, b):
    print(a + b)
    return a, b
add(3, 3)

@only_odd_arguments
def multiply(a, b, c, d, e):
    print(a * b * c * d * e)
    return a, b, c, d, e
multiply(4, 5, 3, 1, 5)
