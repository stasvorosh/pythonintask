# Задача 11, Вариант 12 

#Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python гл. 6).

# Мамедов Р.А.
# 10.05.2016


import random
X = "X"
O = "O"
EMPTY = " "
TIE = "ничья"
NUM_SQUARES = 9
def main():
	return 0
def display_instruct():
	print ('''Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
доски - так. как показано ниже:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Приготовься к бою. Вот-вот начнется решающее сражение.\n ''')
def ask_yes_no(question):
	response = None
	while response not in ("да", "нет"):
		response = input (question).lower()
	return response
	
def ask_number(question, low, high):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response
def pieces():
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (да/нет): ")
    if go_first == "да":
        print("Ну что ж, даю тебе фору, играй крестикаи")
        human = X
        computer = O
    else:
        print("Твоя удаль тебя погубит... Буду начинать я.")
        human = O
        computer = X
    return computer,human
	
def new_board():
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board
	
def display_board(board):
	print ("\n\t", board[0], " | ", board[1], " | ", board[2])
	print ("\t", "-----------")
	print ("\n\t", board[3], " | ", board[4], " | ", board[5])
	print ("\t", "-----------")
	print ("\n\t", board[6], " | ", board[7], " | ", board[8])
	print ("\t", "-----------\n")
	
def legal_moves(board):
	moves =[]
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves
	
def winner(board):
	WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
	return None
	
def human_move(board, human):
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Ваш ход ", 0, NUM_SQUARES)
		if move not in legal:
			print ("Смешной человек! Это поле уже занято")
	return move
	
def computer_move(board, computer, human):
	#создаем копию доски
	board = board[:]
	# приоритет полей
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	print ("Я выберу поле номер", end=" ")
	for move in legal_moves(board):
		board[move] = computer
		#если ход ведет к победе, то выбираем его
		if winner(board) == computer:
			print (move)
			return move
		board[move] = EMPTY
	for move in legal_moves(board):
		board[move] = human
		if winner(board) == human:
			print (move)
			return move
		board[move] = EMPTY
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print (move)
			return move
def next_turn(turn):
	if turn == X:
		return O
	else:
		return X
		
def congrat_winner(the_winner, computer, human):
	if the_winner != TIE:
		print (the_winner, "побеждают")
	else:
		print ("Ничья")
	if the_winner == computer:
		print ("Как я и предсказывал, победа в очередной раз осталась за мной")
	elif the_winner == human:
		print ("О нет, неужели ты перехитрил меня")
	
def game():
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
	
if __name__ == '__main__':
	main()
	game()
	input ("Нажмите Enter, чтобы выйти")