#num_len program
def num_len(number):
    count = 0
    while number: #циклом прохожу количество раз целочисленным делением и считаю количество проходов (count)
        count += 1
        number //= 10
    print('Кількість чисел: ', count)

num_len(5474565)