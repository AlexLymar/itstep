def multiple(s):
    count = 0
    while True:
        count += s
        yield count

gen_multiple_of_two = multiple(2)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))

gen_multiple_of_thirteen = multiple(13)
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print('----закоментований скрипт робочий-----------------')
#def multiple():
#   s = [i + i for i in range(1, 10)]
#   for i in s:
#        yield i
#
#gen_multiple_of_two = multiple()
#print(next(gen_multiple_of_two))
#print(next(gen_multiple_of_two))
#print(next(gen_multiple_of_two))
#print(next(gen_multiple_of_two))
#print(next(gen_multiple_of_two))

def only_odd_arguments(func):
    def wrapper(*args):
        n = func(*args)
        if n % 2 != 0:
            return func(*args) * func(*args)
        else:
            print('Please add numbers')

    return wrapper

@only_odd_arguments
def rez_funcion(a: int, b: int):
    print('a + b = ', (a + b))
    return a + b
print('a * b = ', rez_funcion(5, 5))




