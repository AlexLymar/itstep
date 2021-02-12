# rainbow program
color = input('Input number color rainbow 1 to 7 - ')
try:
    color = int(color)

    rainbow = {
        1: 'Red',
        2: 'Orange',
        3: 'Yellow',
        4: 'Green',
        5: 'Blue',
        6: 'Indigo',
        7: 'Violet',
       }

    if color == 7:
        print(rainbow[color], rainbow[color - 1])
    elif color == 0:
        print('This color does not exist')
    elif (color <= 7) and color > 0:
        print(rainbow[color], rainbow[color + 1], rainbow[color - 1])
    elif color >= 8 and (color < 0):
        print('You entered an invalid value')
    else:
        print('You made a mistake, repeat with rainbow from 1 to 7')
except:
    print('input integer number, please..')

