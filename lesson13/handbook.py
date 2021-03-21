
def handbook(ident, phone, users):
    while True:
        print('''
        ----------------------------------------
        1. Показати списки
        2. Відсортувати список по ідентифікаційному номеру
        3. Відсортувати список по телефонам
        4. Вивести список користувачів, з кодами та телефонами.
        5. Вихід з програми
        ''')
        user_input = input('Яку дію виконуємо? ')
        if user_input == '1':
            print(ident)
            print(phone)
            print(users)
        elif user_input == '2':
            ident.sort()
            print(ident)
        elif user_input == '3':
            phone.sort()
            print(phone)
        elif user_input == '4':
            zipper = zip(users, ident, phone)
            print(list(zipper))
        elif user_input == '5':
            exit()
        else:
            print('Введено невірне значення')

ident = [2334, 4532, 8767, 3354]
phone = [2554953, 2356959, 2012701, 1423477]
users = ['Вася', 'Петя', 'Гриша', 'Даша']
handbook(ident, phone, users)