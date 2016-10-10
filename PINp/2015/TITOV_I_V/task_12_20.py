# Задача 12
# Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python
#гл. 6).

# Titov I. V.
# 02.06.2016

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Инструкции"""  
    print(
    """
    Да начнётся битва!  

    На своём ходу, введи цифру, согласно рисунку:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    GOGOGO!!! \n
    """
    )


def ask_yes_no(question):
    """Вопрос да/нет"""
    response = None
    while response not in ("д", "н"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Первый ход"""
    go_first = ask_yes_no("Берёшь первый ход? (д/н): ")
    if go_first == "д":
        print("\nТвои кресты")
        human = X
        computer = O
    else:
        print("\nНуль значит любишь")
        computer = X
        human = O
    return computer, human


def new_board():
    """Ноовое поле"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Вывести поле на экран"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Возможные ходы"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определить победителя"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Ход игрока"""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭтот квадрат занят\n")
    print("Хорошо...")
    return move


def computer_move(board, computer, human):
    """Компьютер делает ход"""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Я выберу поле", end=" ")
    
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Изменить ход"""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Поздравление победителя"""
    if the_winner != TIE:
        print(the_winner, "выиграл!\n")
    else:
        print("ничья!\n")

    if the_winner == computer:
        print("Я выиграл \n")

    elif the_winner == human:
        print("Ну всё")

    elif the_winner == TIE:
        print("Не обижайся, бери ичью")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nНажмите ENTER длы выхода")
