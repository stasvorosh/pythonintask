# Задача 12. Вариант 23
# Разработайте игру "Крестики-нолики".
#(см. М.Доусон Программируем на Python гл. 6).

# Moshkov Y. O.
# 20.05.2016

from tkinter import *

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
        if self.checkWin():
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
    def checkWin(self):
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

# GUI

def act(num, game, button):
    state = game.move(num)
    if state > 0:
        if game.crturn:
            button["text"] = 'X'
        else:
            button["text"] = 'O'
        if state == 2:
            winner = "Нолики"
            if game.crturn:
                winner = "Крестики"
            if (messagebox.askquestion("Победа!", winner +
                                           " выиграли. Начать заново?")) == "yes":
                newGame(buttons)
                game.clear()
                game.crturn = True
            else:
                gui.destroy()
        else:
            game.crturn = not game.crturn

def newGame(buttons):
    for btn in buttons:
        btn["text"] = ''

gui = Tk()
buttons = []
for i in range (9):
    buttons.append(Button(gui, text = "", font = "arial, 48", width = 3,
                          command = lambda i = i: act(i, game, buttons[i])))
    buttons[i].grid(row = int(i / 3), column = i % 3)
gui.mainloop()
