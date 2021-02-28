# tictactoe program
board = list(range(0, 9))       # Основний лист, який дасть змогу ідентифікувати комірки для гри
wins_lst = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] # Тут описані всі виграшні комбінації

def drw_board():        # Функція, яка мені намалює ігрове поле із значеннями комірок
    print('-------------')
    for i in range(3):  # циклом перебираю список 0-2 перший рядок, 3-5 другий рядок та 6-8 третій
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')

def take_input(player_zn):
    while True:
        znach = input('Ваш хід: ' + player_zn)
        if not (znach in '012345678'):  # перевіряю, що було введено з клавіатури,
                                        # якщо znach є в рядку (012345678) то перевожу її на int(), якщо ні - то наступна спроба вводу
            print('Помилка вводу числа, спробуйте ще раз!')
            continue
        znach = int(znach)
        if str(board[znach]) in 'XO':  # тут перевіряю, чи вже була задіяна дана комірка
            print('Комірка занята! Спробуйте ще раз..')
            continue
        board[znach] = player_zn
        break

def win():
    for i in wins_lst:      # тут перебираю, всі виграшні комбінації, які описані win_lst, якщо є співпадіння, то гру закінчено
        if (board[i[0]]) == (board[i[1]]) == (board[i[2]]):
            return board[i[0]]
    else:
        return False

def tictactoe():            # Функція, яка мені наглядно показала "ПРОПАСТЬ" в моїх знаннях. Отут моє слабе місце!!! Зліпити до кучі все.
    count = 0
    while True:
        drw_board()         # малюю ігрове поле
        if count % 2 == 0:  # логіка чередування вводу Х
            take_input('X')
        else:
            take_input('O') # логіка чередування вводу О
        if count > 3:       # тут запускаю функцію win на перевірку результатів гри, якщо є співпадіння в win_lst то об'являється переможець
            winner = win()  # тут точка входу в функцію, яка визначить результат гри
            if winner:
                print(winner, 'Виграв')
                break
        count += 1          # змінна, яка визначатиме запуск функції win
        if count > 8:
            drw_board()
            print('Нічия!')
            break
tictactoe()

## Признаюсь, слідуючий код (НИЖЧЕ) взяв з книжки посібника Доусона, але так і не зрозумів його логіку (він частково робочий)
## багато часу на нього витратив, рука не піднімається його видалити.
############# В цьому коді, я до кінця не розібрався за браком часу по здачі роботи, але хотів цей варіант представляти #################

#X = 'X'
#O = 'O'
#empty = ' '
#tie = 'Ничья'
#num_squares = 9
#def display_instruct():
#    print(
#    """
#    Добро пожаловать на ринг игры "Крестики-нолики".
#    Чтобы сделать ход, введи число от 0 до 8.
#    Числа соответствуют полям доски, как показано ниже:
#    0 | 1 | 2|
#    ----------
#    3 | 4 | 5|
#    ----------
#    6 | 7 | 8
#    Приготовься к бою!!
#    вот-вот начнётся решающая битва!\n
#    """)
#def ask_yes_no(question):
#    response = None
#    while response not in ('y', 'n'):
#        response = input(question).lower()
#    return response
#
#def ask_number(question, low, hight):
#    response = None
#    while response not in range(low, hight):
#        response = int(input(question))
#    return response
#
#def pieces():
#    go_first = ask_yes_no('Хочешь ходить первым? (y/n):')
#    if go_first == 'y':
#        print('\nИграй крестиками!')
#        human = X
#        computer = O
#    else:
#        print('Ок! Буду начинать я!!')
#        human = O
#        computer = X
#    return computer, human
#
#def new_board():
#    board = []
#    for square in range(num_squares):
#        board.append(empty)
#    return board
#
#def display_board(board):
#    print('\n\t', board[0], '|', board[1], '|', board[2])
#    print('\t', '------------')
#    print('\n\t', board[3], '|', board[4], '|', board[5])
#    print('\t', '------------')
#    print('\n\t', board[6], '|', board[7], '|', board[8], '\n')
#
#def legal_moves(board):
#    moves = []
#    for square in range(num_squares):
#        if board[square] == empty:
#            moves.append(square)
#        return moves
#def winner(board):
#    ways_to_win = ((0, 1, 2),
#                   (3, 4, 5),
#                   (6, 7, 8),
#                   (0, 3, 6),
#                   (1, 4, 7),
#                   (2, 5, 8),
#                   (0, 4, 8),
#                   (2, 4, 6))
#    for row in ways_to_win:
#        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
#            winner = board[row[0]]
#            return winner
#        if empty not in board:
#            return tie
#        return None
#
#def human_move(board, human):
#    legal = legal_moves(board)
#    move = None
#    while move not in legal:
#        move = ask_number('Твой ход', 0, num_squares)
#        if move not in legal:
#            print('Это поле уже занято, выбери другое.\n')
#        return move
#
#def computer_move(board, computer, human):
#    board = board[:]
#    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
#    print('Я выберу поле номер', end=' ')
#    for move in legal_moves(board):
#        board[move] = computer
#        if winner(board) == computer:
#            print(move)
#            return move
#        board[move] = empty
#    for move in legal_moves(board):
#        board[move] = human
#        if winner(board) == human:
#            print(move)
#            return(move)
#        board[move] = empty
#    for move in best_moves:
#        if move in legal_moves(board):
#            print(move)
#            return move
#
#def next_turn(turn):
#    if turn == X:
#        return O
#    else:
#        return X
#
#def congrat_winner(the_winner, computer, human):
#    if the_winner != tie:
#        print('Три', the_winner, 'в ряд!\n')
#    else:
#        print('Ничья!\n')
#    if the_winner == computer:
#        print('Я тебя сделал!')
#    elif the_winner == human:
#        print('Неможет быть...??')
#    elif the_winner == tie:
#        print('В этот раз ничья!!')
#
#def main():
#    display_instruct()
#    computer, human = pieces()
#    turn = X
#    board = new_board()
#    display_board(board)
#    while not winner(board):
#        if turn  == human:
#            move = human_move(board, human)
#            board[move] = human
#        else:
#            move = computer_move(board, computer, human)
#            board[move] = computer
#        display_board(board)
#        turn = next_turn(turn)
#    the_winner = winner(board)
#    congrat_winner(the_winner, computer, human)
#main()
#input('\n\nНажмите Enter, для выхода')