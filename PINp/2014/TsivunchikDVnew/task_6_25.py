# Задание 6. Вариант 25.
# Создайте игру, в которой компьютер загадывает название одного из четырех
# океанов Земли, а игрок должен его угадать.
# Цивунчик Денис Владимирович
# 27.05.2016

import random

guessesTaken = 0

print("Привет, отгадай один из четрыех океанов Земли.")
x = random.choice(["Северный Ледовитый", "Атлантический", "Индийский", "Тихий"])

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
