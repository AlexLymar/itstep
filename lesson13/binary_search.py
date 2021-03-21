print('----------line search program------------')


def search(search_num):
    count = 1
    print('Line searsh value in: ', search_num)
    user_input = input('Enter value for line search: ')
    while True:
        for i in search_num:
            if i != user_input:
                    count += 1
            else:
                print('Search value: ', user_input, '\n', 'Value loops: ', count)
                break
            if user_input not in search_num:
                print('No search value')
                break
        break
search_num = ['1', '35', '12', '4', '3', '13', '9', '15', '19', '21']
search(search_num)

print('\n--------binary search program-------------')


def binary_search(srt_lst, x, low, higt):
    mid = (low + higt) // 2
    count = 0
    while srt_lst[mid] != x and low <= higt:
        count += 1
        if x > srt_lst[mid]:
            low = mid + 1
        else:
            higt = mid - 1

        mid = (low + higt) // 2
    if low > higt:
        print('Значення не знайдено')
    else:
        print('Значення знайдено: ', x, '\n', 'Кількість циклів: ', count)

lst = [1, 12, 4, 3, 13, 9, 15, 19, 21, 18]
print(lst)
srt_lst = sorted(lst)
low = 0
higt = len(lst) - 1
x = int(input('Введіть значення для пошуку елемента\n '))
binary_search(srt_lst, x, low, higt)
