#user_pyramid program
rows = int(input('Введите размер пирамиды - '))
for i in range(rows):
    print(' '*(rows-i-1) + '*'*(2*i+1))
