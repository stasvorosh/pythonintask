# Задание 7. Вариант 10.
# Разработайте систему начисления очков для задачи 6, в соответствии с
# которой игрок получал бы большее количество баллов за меньшее количество
# попыток.
# Колеганов Никита Сергеевич
# 29.05.2016

import random

guessesTaken = 0

print("Привет, отгадай одну из стран Тройственного Союза")
x = random.choice(["Германия", "Австро-Венгрия", "Италия"])

while guessesTaken < 10:
      print("Я загадала: ")
      guess = input()

      guessesTaken = guessesTaken + 1
      
      if guess != x:
          print("Неверно.")
      if guess == x:
          break

if guess == x:
      print("Верно! Число попыток:", guessesTaken)
      if guessesTaken == 1:
          print("Баллов заработано:", 100)
      if guessesTaken == 2:
          print("Баллов заработано:", 90)
      if guessesTaken == 3:
          print("Баллов заработано:", 80)
      if guessesTaken == 4:
          print("Баллов заработано:", 70)
      if guessesTaken == 5:
         print("Баллов заработано:", 60)
      if guessesTaken == 6:
          print("Баллов заработано:", 50)
      if guessesTaken == 7:
          print("Баллов заработано:", 40)
      if guessesTaken == 8:
          print("Баллов заработано:", 30)
      if guessesTaken == 9:
          print("Баллов заработано:", 20)
      if guessesTaken == 10:
          print("Баллов заработано:", 10)
if guess != x:
      print("Попытки кончились.")
      print("Вы не набрали баллов.")

input("\n\nНажмите Enter для выхода.")
