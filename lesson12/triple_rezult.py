def triple_rezult():
    s = [i * 3 for i in range(1, 10)]
    return s

s1 = triple_rezult()
print(s1)
print('--------образец-------------')

##############################################################
def decorator(func):
    def wrapper():
        print('HELLO')
        func()
        print('BYE')
    return wrapper

@decorator
def show():
    print('Не сдавайся!!!')

show()
print('------------------------------------')

# triple_rezult program
def triple_rezult(func):
    def wrapper(*args):
        return func(*args) * 3
    return wrapper

@triple_rezult
def rez_funcion(a: int, b: int):
    print('a + b = ', (a + b))
    return a + b

print('(a + b) * 3 = ', rez_funcion(5, 3))
