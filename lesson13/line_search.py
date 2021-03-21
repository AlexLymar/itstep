
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