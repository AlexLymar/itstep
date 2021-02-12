#old_school program
ext = 1
while ext > 0:
    try:
        print('Введите 0 для выхода')
        x = int(input('Хочу вывести таблицу умножения на: '))
        if x > 10 or x < 0:
            print('Введите число от 1 до 10')
            break
        if x == 0:
            ext -= 1
            print("Пока!!!")
            exit()
        y = 1
        a = 1
        count = 0
        while y <= 10:
            print(a, ' X ', x, ' = ', a * x)
            a += 1
            y += 1
            count += 1
    except ValueError:
        print('Введите целое число')