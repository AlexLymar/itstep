x = int(input('Input integer x of range 1 -100 - '))

if x > 100 or x < 0 in range(101):
    print('Out of range')
    exit()

if x % 3 == 0 and x % 5 == 0:
    print('FizzBuzz')
elif x % 3 == 0:
    print('Fizz')
elif x % 5 == 0:
    print('Buzz')

exit()