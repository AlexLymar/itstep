from functools import reduce

lst = [1, 3, 6, 8, 10]
rezult = reduce((lambda x, y: x * y), lst)
print(rezult)
