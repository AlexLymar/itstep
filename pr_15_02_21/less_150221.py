first_list = ['Neo', 'Trinity', 'Morphius', 'Mouse']
second_list = ['Matrix', 'Food', 'Lesson', 'Apple']
output_list = []
for i in first_list:
    for j in second_list:
        i += j
        output_list.append(i+' '+j)
print('output_list = ', output_list)
print('---------------------')
#-------------------------------------------------------------
#def funktion_name():
#    print('Я только учусь))')
#
#
#def hello_function():
#    names = ['John', 'July', 'Marvolo']
#    print('Hello!')
#    for i in names:
#        print('Hello!', i)
#        print('------------------------------')
#
#funktion_name()
#hello_function()
##-------------------------------------------------
#def return_power(number, number2, number3, power=2):
#    print()
#    list_with_power = number.copy()
#    for i, elem in enumerate(number):
#        number[i] = elem ** power
#
#    number = [2, 4, 5, 6]
#    result = return_power(number = number2)
#print(result)
#print(number2)
#
#def take_arg(*args, **key_value_dict):
#    for i in argus:
#        print(i)
#
#def range_sum(start_range, end_range):
#    if start_range > end_range:
#        start_range, end_range = end_range, start_range
#    res = 0
#    while start_range <= end_range:
#        res = res + start_range
#        start_range += 1
#    return res
#
#def range_sum2(start_range, end_range):
#    return sum(list(range(start_range, end_range + 1)))
#print(range_sum2(sum([1, 4])))
#
#print(range_sum(1, 4))

def prime_number(number):
    if number <= 1 or number < 0:
        return None
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

res = prime_number(10)
#res2 = prime_number(149)
print(res)
#print(res2)

# Задание 2
def num(x, y):
    list=[]
    for i in range(x, y):
        if i % 2 != 0:
          list.append(i)
    print(list)
num(3, 10)

# Задание 3
def line(x = 1, y = 7, z = 3):
    row = '#'
    for i in range(x, y):
        print(row)

line()

