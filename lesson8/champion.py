# champion program
c = 1       #тут, до начала цикла while, объявляю нужные переменные и один пустой лист, их начальные значения.
lst = []
minimum = 0
maximum = 0
sr = float()
zag_k = 0
while c > 0:    #переменную (с) уже объявлено > 0 выше
    try:
        q = input(('Введіть кількість повторів в підході № %s або stop для припинення: ') % c)
        q = q.lower()   #Тут делаю "уравняловку" по вводу текста с регистром... На отрицательные числа в примере небыло - значит можна!
        if q == 'stop':     # Если ввели:(StOp, STOP, stop, sToP, STOP или как-то так) то мы выводим результаты работы и выходим наружу.
            print('Кількість підходів: ', c - 1)        # в этой строке находится коррекция подсчёта счётчика
            print('Загальна кількість повторень ', zag_k)
            print('Максимальна кількість повторень ', maximum)
            print('Мінімальна кількість повторень ', minimum)
            print('Середня кількість повторень ', sr)
            break       # ... выйдет из цикла

        else:       # тут условие перевода строки int введённых данных + вычисление "Загальних даних" [zag_k]
            q = abs(int(q))  # перевожу переменную в положительное число
            zag_k = zag_k + q

        lst.append(q)       # здесь "святая-всех-святых" - лист в который попадают данные и мы отсюда берём значения
        c += 1      # тот-же самый count(счётчик)
        maximum = max(lst)  #максимальное значение из "святая-всех-святых" - lst
        minimum = min(lst)  #минимамальное значение из "святая-всех-святых" - lst
        sr = sum(lst) / len((lst))      # здесь вычисляем среднее значение (опять же: "святая-всех-святых")

    except ValueError:      # тут, если пользователь ввёл не то
        print('Помилка вводу даних. Введіть число.')
        c = c + 0       # Счётчик коррекции введённых неправильных данных