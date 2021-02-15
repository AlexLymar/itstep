#rot13 program
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
end = 1
while end > 0:
    try:    # Здесь описаны, условия для того, что-бы программа не крашилась
        print('Input 0 for exit')
        encrypt = input('Enter message: ')
        if encrypt == '0':
            print('Bye!!')
            exit()
        key = int(input('Enter key for crypt 1-25: '))
        if key < 0 or key > 25:
            print('Enter key 1-25')
            continue

        encrypt = encrypt.lower() #перевод текста в нижний регистр
        crypt = ''
        for i in encrypt:
            pos = alphabet.find(i)      # ищу первое совпадение в alphabet и возвращаю порядковый номер искомого символа
            new_pos = pos + key         # к найденому значению добавляю значение ключа
            if i in alphabet:
                crypt += alphabet[new_pos]      # нахожу новый индекс для буквы
            else:
                crypt += i      # если введено другие символы то добавляю и их
        print('You crypto result is: ', crypt)
        print('-----------------------------------')
        decrypt = ''
        for i in crypt:
            dec = alphabet.find(i)      # ищу первое совпадение в alphabet и возвращаю порядковый номер искомого символа
            decnew_pos = dec - key      # от найденого значения вычитаю значение ключа
            if i in alphabet:
                decrypt += alphabet[decnew_pos]     # нахожу прежний индекс для буквы
            else:
                decrypt += i    # если введено другие символы то добавляю и их
        print('You decrypto result is: ', decrypt)
    except ValueError:
        print('input integer number 1-25')
