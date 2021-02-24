#buble_sort program
def buble_sort(num_list, reverse):
    for i in range(len(num_list) - 1, 0, -1): #выбираю правило выборки в листе (i), последнее значение будет исключаться для повторной проверки цикла
        for j in range(i):                    #пробегаю по содержимому листа и выполняю условия сортировки значений согласно True/False
            if reverse == True:
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            else:
                if num_list[j] < num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    print('Результат: ', num_list)
    print(reverse)

reverse = False
num_list = [1, 6, 23, 97, 43, 22, 13, 0, 5, 8]
print('Изначально:', num_list)
buble_sort(num_list, reverse)