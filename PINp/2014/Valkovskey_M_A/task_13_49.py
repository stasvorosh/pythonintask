# Задача 13. Вариант 49.
#Разработайте собственную стратегию ходов компьютера для игры "Крестики-нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой стратегией. 
#Valkovskey M.A.
from random import randint


size = 3

board = [ 0 ] * size * size
pics = [' . ', ' x ', ' o ']


def print_board (board):
  print()

 
  for num in range(size):
    print('  ' + str(num +1) + ' ', end='')

  print()

  
  index = 1
  letter = 97
  for cell in board:
    print('|', end='')
    print(pics[cell], end='')
    if index == size:
      print('| ' + chr(letter))
      letter += 1
      index = 0
    index += 1
  print()


def check_board (board, silent=False):
  
  for row in range(size):
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell*size] == board[row]:
          count += 1
        else:
          break
      if count == size:
        if not silent:
          print_board(board)
          print('x' if board[row] == 1 else 'o', 'is winner!')
        return True

  
  for row in range(0, size * size, size):
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell] == board[row]:
          count += 1
        else:
            break
      if count == size:
        if not silent:
          print_board(board)
          print('x' if board[row] == 1 else 'o', 'is winner!')
        return True

 
  for row in [0, size-1]:
    if board[row] in [1, 2]:
      count = 0
      for cell in range(size):
        if board[row+cell*(size + (1 if row==0 else -1))] == board[row]:
          count += 1
        else:
          break
      if count == size:
        if not silent:
          print_board(board)
          print('x' if board[row] == 1 else 'o', 'is winner!')
        return True

  
  if 0 not in board:
    if not silent:
      print_board(board)
      print('draw!')
    return True


print('\nWelcome! Make your turns like this - \'2a\' or \'3c\'')
print('You - x, computer - o')
ixes = True

while True:
  print_board(board)
  
  if ixes:
    turn = input('human (x) turn > ')
    try:
      index = ( int(turn[0]) -1 +
               (ord(turn[1]) -97) * size )
      if board[index] in [1, 2]:
        raise
      board[index] = 1
    except:
      print('invalid value', turn)
    else:
      if check_board(board):
        break
      ixes = False
  
  else:
    print('comuter turn. . .')
    best_turn = (-1, size*size*size)
    k = 20
    for k in range(6000):
      copy = board[:]
      first = -1
      for n in range(size*size*size):
        index = randint(0, size*size - 1)
        if copy[index] in [1, 2]:
          continue
        if first == -1:
          first = index
        copy[index] = (1 if ixes else 2)
        if check_board(copy, True):
          if not ixes:
            
            if n < best_turn[1]:
              best_turn = (first, n)
            break
          else:
            
            best_turn = (index, n)
        ixes = not ixes

    board[best_turn[0]] = 2
    if check_board(board):
        break
    ixes = True

input('Press Enter..')
