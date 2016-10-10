# Задача 13
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-
#нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой
#стратегией.

# Denisenko A. N.
# 02.06.2016

import random

def instruction ():
    print (
        """
              Крестики-нолики
Раз в десятелетие компьютер и человек сходятся в эпической битве
В битве ТИТАНОВ
Я надеюсь ты готов!!! УХАХАХАХААХА
P. S. Возможны жертвы, 18+ блаблабла, формальности

Во время своего хода вбей цифру (0-8) согласно рисунку ниже:
\t0 | 1 | 2
\t---------
\t3 | 4 | 5
\t---------
\t6 | 7 | 8

        """)#Начальные инструкции

def level_difficulty ():
    userVvod = None
    while userVvod not in range (1,3):
        userVvod = int (input("Выбери уровень сложности: 1 - очень просто (рандомные ходы)\n2 - средне (тактика Mr. Dounson)"))
    return userVvod #Выбор сложности    

def choise_figure ():
    userVvod = None
    while userVvod != "д" and userVvod != "н":
        userVvod = input ("Берёшь первый ход (то бишь крестики)? (д/н) ")
        userVvod.lower()
    if userVvod == "д":
        return "X","O"
    else:
        return "O", "X" #Выбор первого хода, первое, что возвращается - выбор игрока 

def create_board ():
    propusk = " "
    firstboard = []
    for i in range (9):
        firstboard.insert (i, propusk)
    return firstboard #Создаёт доску

def vision_board (board):
    this_board = board[:]
    field = 0
    for i in range (3):
        for j in range (3):
            print (this_board[field], end = "")
            field +=1
            if j != 2:
                print (" | ", end = "")
            else:
                print()
        if i != 2:
            print ("---------")#вывод доски 


def search_theory_step (board):
    this_board = board[:]
    theory_step = []
    for i in range (9):
        if this_board[i] == " ":
            theory_step.append(i)
    return theory_step #Массив возможных вариантов

def step_human (board):
    this_board = board[:]
    this_theory_step = search_theory_step (this_board)
    userVvod = int (input("Ваш ход: "))
    while userVvod not in this_theory_step:
        userVvod = int (input ("ОШИБКА. Ещё раз: "))
    return userVvod #Ход человека

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != " ":
            winner = board[row[0]]
            return winner
    if " " not in board:
        return "TIE"
    return None

def step_comp(board, level, computer, human):
    if level == 1:
        return step_easy_comp(board)
    if level == 2:
        return step_mid_comp(board, computer, human)

def step_easy_comp (board):
    nomer = random.choice(search_theory_step (board))
    print ("Мой ход - ",nomer)
    return nomer

def step_mid_comp(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    for move in search_theory_step(board):
        board[move] = computer
        if winner(board) == computer:
            print ("Мой ход - ", move)
            return move
        board[move] = " "
    for move in search_theory_step(board):
        board[move] = human
        if winner(board) == human:
            print ("Мой ход - ", move)
            return move
        board[move] = " "
    for move in BEST_MOVES:
        if move in search_theory_step(board):
            print ("Мой ход - ", move)
            return move

def who_winner (stroka, computer, human) :
    if stroka == "TIE":
        print ("Ойойой, перепутал немного... Гордись ничейкой, человечек")
    elif stroka == human:
        print ("Поздравляю (я поддавался) жалкое (я поддавался) пресмыкающееся (да я честно поддавался)")
    else:
        print ("О даааа, ну я играл одним пальцем, лёгкая победка")

def main():
    instruction()#вывели инструкцию
    level = level_difficulty() # Выбрали сложность
    human, computer = choise_figure() # Выбор кто чем играет
    board = create_board() #создали доску
    if human == "X":
        chod = 1
    else:
        chod = 2
    while  not winner(board):
        if chod % 2 == 1:
            board[step_human(board)] = human
            vision_board(board)
            chod+=1
        else:
            board[step_comp(board,level,computer, human)] = computer
            chod+=1
            vision_board(board)
    who_winner(winner(board), computer, human)
    
main()
input("\n\nНажмите Enter для выхода.")
