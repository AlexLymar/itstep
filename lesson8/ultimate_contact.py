#ultimate_contact program
first_list = ['Neo', 'Trinity', 'Mouse']
# верхний список нужно "соединить" с нижним по каждому исходному значению
# тоесть один(верхний) ко всем(нижний)
second_list = ['Matrix', 'Forever', 'Alone']
output_list = []                        #сюда будет помещён результат
for i in first_list:                    # перебираю список на выявление содержимого 1 списка
    for j in second_list:               #  перебираю список 2 на выявление содержимого
        output_list.append(i+' '+j)     # здесь проходит слияние 1 к многим

print('first_list = ', first_list)      # Вывод на дисплей
print('second_list = ', second_list)
print('output_list = ', output_list)