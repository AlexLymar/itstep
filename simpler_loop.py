#simpler_loop program
x = 1
y = 0
count = 0
while x > 0:
    x += 1
    y = x
    if x % 5 == 0:
        print(y, 'делится на 5')
        count += 1
        if count >= 30:
            print('Общее число найденых чисел: ', count)
            exit()