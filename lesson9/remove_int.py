print('remove_int program:')
values_list = [1, 4, 3, 1, 2, 6, 3, 2, 1, 1, 7, 4, 5, 5]
def remove_int(values_list, num):

    lst = []
    for n in values_list:       #определяю наличие указанного значения в листе, и если оно есть то исключаю его внесение в новый лист
        if num != n:
            lst.append(n)

    print('Исходный лист: ', values_list)
    print('Результат   - :', lst)
    print('Кол-во удалённых объектов: ', len(values_list) - len(lst))
    print('Значение удалённого объекта', num)

remove_int(values_list, 1)