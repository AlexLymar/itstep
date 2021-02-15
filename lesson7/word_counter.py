# word_counter program
stroka = input('Input text: ')
x = stroka.count(' ') + 1 #подсчёт слов по признаку "пробел", но так как машина отсчёт ведёт с нуля,
                          # то добавляю 1 для визуального совпадения

print('Quantity words: ', x)