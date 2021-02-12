a = input('Input a - ')
b = input('Input b - ')

while a.isdigit() == False:
    print('Am i a Joke to You?')
    break
while b.isdigit() == False:
    print('Am i a Joke to You?')
    break

if a > b:
    print(a, b)
if a == b:
    print('EQUALS')
if b > a:
    print(b, a)
