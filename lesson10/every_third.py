# every_third program
def every_third(one, two):
    end = 1
    while end > 0:
        try:
           one = int(input('Введіть перше число: '))
           two = int(input('Введіть друге число ')) + 1
           if one > two:
               print('Введене значення повинно бути більше за попереднє!!')
           else:
               break
        except ValueError:
            print('Ви ввели невірне значення')
    even_list = []
    list_generate = []
    for i in range(one, two):
        even_list.append(i)
#            print('Парні числа: ', ([x for x in even_list if x % 2 == 0])) # чисто екпериментальний рядок
    for j in even_list:
        if j % 2 == 0:
            list_generate.append(j)
    print('Введений діапазон чисел: ', even_list)
    print('Знайдені парні числа: ', list_generate)

# every_third program
    print('\n-----for every_third code-------------------\n')

    def even_list_generate():
        nonlocal one
        nonlocal two
        nonlocal even_list
    lst_rezult = []
    for i in even_list[2::3]:
            lst_rezult.append(i)
    print('Числа, які були використані для формування діапазону:', one, ' та ', two-1)
    print('Кожне третє значення вказаного діапазону: ', lst_rezult)



every_third(0, 0)