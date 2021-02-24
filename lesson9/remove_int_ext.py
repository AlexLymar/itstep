print('remove_int_ext program:')
values_list = [1, 2, 1, 3, 6, 3, 2, 1, 5]
print('Исходный лист: ', values_list)

def remove_int_ext(values_list, num):
    c = 0                       #счётчик найденых и удалённых значений

    for n in values_list:       #Сравниваю указанное значение в листе, и если есть совпадение то удаляю
        if num == n:
            values_list.remove(num)
            c += 1
        else:
            pass

    print('Результат  - : ', values_list)
    print('Кол-во удалённых объектов: ', c)
    print('Значение удалённого объекта:', num)

remove_int_ext(values_list, 1)
