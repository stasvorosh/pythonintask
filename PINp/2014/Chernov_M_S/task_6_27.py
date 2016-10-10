# Задание 6. Вариант 27.
# Создайте игру, в которой компьютер загадывает имя одного из двух братьев,
# создателей старославянской азбуки, а игрок должен его угадать.
# Чернов Михаил Сергеевич
# 28.05.2016

import random

guessesTaken = 0

print("Привет, отгадай одного из основателей азбуки.")
x = random.choice(["Кирилл", "Мефодий"])

while guessesTaken < 6:
      print("Я загадала: ")
      guess = input()

      guessesTaken = guessesTaken + 1

      if guess != x:
          print("Неверно.")
      if guess == x:
          break

if guess == x:
      print("Верно! Число попыток:", guessesTaken)
      
if guess != x:
      print("Попытки кончились.")

input("Нажмите Enter для выхода.")
