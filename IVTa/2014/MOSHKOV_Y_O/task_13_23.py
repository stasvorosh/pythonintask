# Задача 13. Вариант 23
# Разработайте игру "Крестики-нолики".
#(см. М.Доусон Программируем на Python гл. 6).

# Moshkov Y. O.
# 21.05.2016

from tkinter import *
import random

class Game:
    crturn = True
    field = []
    def __init__(self):
        for i in range (3):
            self.field.append(['', '', ''])
    def move(self, pos):
        state = 0
        if self.fill_pos(pos):
            state = 1
        if self.check_win():
            state = 2
        return state
    def fill_pos(self, pos):
        if self.crturn:
            if self.field[int(pos / 3)][pos % 3] == '':
                self.field[int(pos / 3)][pos % 3] = 'X'
                return True
        else:
            if self.field[int(pos / 3)][pos % 3] == '':
                self.field[int(pos / 3)][pos % 3] = 'O'
                return True
    def check_win(self):
        if self.crturn:
            unit = 'X'
        else:
            unit = 'O'
        # Rows
        for row in self.field:
            win = True
            for i in row:
                if i != unit:
                    win = False
            if win == True:
                return True
        # Columns
        for col in range (3):
            win = True
            for row in range (3):
                if self.field[row][col] != unit:
                    win = False
            if win == True:
                return True
        # Diagonals
        for i in range (0, 3, 2):
            win = True
            for j in range (3):
                if self.field[i + j * (i * -1 + 1)][j] != unit:
                    win = False
            if win == True:
                return True
    def clear(self):
        for i in range (3):
            for j in range (3):
                self.field[i][j] = ''
                

game = Game()

def act(num, game, button):
    game.crturn = True
    state = game.move(num)
    if state > 0:
        button["text"] = 'X'
        if state == 2:
            quiz(1)
        else:
            game.crturn = False
            if not move_ai(game, 'O'):
                move_ai(game, 'X')
            if (game.check_win()):
                quiz(2)

def move_ai(game, ch_unit):
    # Rows
    for i in range (3):
        aim = check_line_ai(game.field, i, 1, ch_unit)
        if aim is not -1:
            if fill(i, aim, game.field):
                return True
    # Columns
    for i in range (3):
        aim = check_line_ai(game.field, i, 2, ch_unit)
        if aim is not -1:
            if fill(aim, i, game.field):
                return True
    # Diagonals
    for i in range (0, 3, 2):
        aim = check_line_ai(game.field, i, 3, ch_unit)
        if aim is not -1:
            if fill(i + aim * (i * -1 + 1), aim, game.field):
                return True
    # Checks if there is any free cells left
    if not isFree(game.field):
        quiz(3)
        return True
    # Checks for previous moves if found no better alternatives
    if ch_unit == 'X':
        for row in range(3):
            choice = False
            for col in range(3):
                if game.field[row][col] is 'O':
                    choice = True
                if game.field[row][col] is 'X':
                    choice = False
            if choice:
                for col in range(3):
                    if fill(row, col, game.field):
                        return True
        # First move
        while True: 
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if fill(row, col, game.field):
                break
        
def fill(row, col, field):
    if field[row][col] is '':
        field[row][col] = 'O'
        buttons[row * 3 + col]["text"] = 'O'
        return True

def newGame(buttons, game):
    for btn in buttons:
        btn["text"] = ''
    game.clear()
    game.crturn = True

def check_line_ai(field, q, mode, ch_unit):
    ctr = 0
    aim = 0
    for j in range (3):
        if mode is 1:
            row = q
            col = j
        elif mode is 2:
            row = j
            col = q
        elif mode is 3:
            row = q + j * (q * -1 + 1)
            col = j
        else:
            return -1
        if field[row][col] is ch_unit:
            ctr += 1
        else:
            if field[row][col] is '':
                aim = j
    if ctr is 2:
        return aim
    return -1

def isFree(field):
    for row in field:
        for i in row:
            if i is '':
                return True
    return False
    
def quiz(mode):
    if mode is 1:
        title = "Victory"
        msg = "Победа"
    elif mode is 2:
        title = "Defeat"
        msg = "Поражение"
    elif mode is 3:
        title = "Draw"
        msg = "Ничья"
    else:
        return
    if message(title, msg) == "yes":
        newGame(buttons, game)
    else:
        gui.destroy()

def message(title, msg):
    msg += ". Начать заново?"
    return messagebox.askquestion(title, msg)

gui = Tk()
buttons = []
for i in range (9):
    buttons.append(Button(gui, text = "", font = "arial, 48", width = 3,
                          command = lambda i = i: act(i, game, buttons[i])))
    buttons[i].grid(row = int(i / 3), column = i % 3)
gui.resizable(width = False, height = False)
gui.mainloop()
