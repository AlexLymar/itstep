#check_prime program
end = 1
kor = 0
while end > 0:
    try:
        print('Input 0 for exit')
        num = int(input('Input integer x: '))
        if num == 0:
            end -= 1
            print('Bye!')
        if num % 2 == 0:
           print('Не входит в диапазон простых чисел')
        else:
           print('Входит в диапазон простых чисел')
    except ValueError:
        print('Input integer number')
