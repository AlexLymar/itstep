# полтора дня "убил" пока допёр как написать код!!!
no_end = 'y'
while no_end == 'y':
    x = float(input('Введите первое значение - '))
    zn = input('Введите значение +, -, /, - ')
    y = float(input('Введите второе значение - '))

    if zn == '+':
        print(int(x) + int(y))
    elif zn == '-':
        print(int(x) - int(y))
    elif zn == '/':
        print(int(x) / int(y))
    elif zn == '*':
        print(int(x) * int(y))
    else:
        print('Вы ввели неверное значение')
    print('Для выхода нажмите любую клавишу...')
    no_end = input('Если хотите продолжить, то нажмите "y" :')






