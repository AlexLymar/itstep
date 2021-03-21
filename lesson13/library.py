
def library(books_name, years):

    while True:
        print('''
        ---------------------------------------------------------------------
        1. Відсортувати по назвам книг;
        2. Відсортувати по рокам випуску;
        3. Вивести список з назвами та роками випуску;
        4. Вихід з програми.
        ''')
        user_input = str(input('Оберіть, номер дії, яку будемо виконувати.. '))
        if user_input == '1':
            print(sorted(books_name))
        elif user_input == '2':
            print(sorted(years))
        elif user_input == '3':
            zipper = zip(books_name, years)
            print(list(zipper))
        elif user_input == '4':
            break
        else:
            print('Введено невірне значення')

books_name = ['А.Нортон, Королева Солнца', 'Эви Немет, UNIX и Linux. Руководство системного администратора 4-е издание', 'Всеволод Нестайко, Тореодори з Васюківки']
years = [1992, 2016, 1973]

library(books_name, years)