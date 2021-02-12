# мозг сломал, но вижу это задание в таком виде наиболее просто и читабельно)))
mon = int(input('Введите месяц от 1 до 12 - '))

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'Desember'
}

if (mon <= 12) and mon > 0:
    print(months[mon])
else:
    print('You made a mistake, repeat with numbers from 1 to 12')










