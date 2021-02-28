# recursion program
def recursion(lst, count, rez_lst):
    for i in lst:
        if count <= 9:      #роблю вибірку перших 10 значень з основного списку
            i += i
            count += 1
            rez_lst.append(i)
        else:
            count = 0
            print(rez_lst)  # виводжу результат вибірки, рядок нижче показує загальну сумму
            print('Загальна сума: ', sum(rez_lst))
            rez_lst = []    # Очищаю лист, для нової порції вибірки

lst = list(range(0, 101))  # Формую лис із значеннями від 0 до 100
count = 0                  # змінна, яка виступає лічильником
rez_lst = []               # Сюди буду класти результат роботи вибірки
recursion(lst, count, rez_lst)
