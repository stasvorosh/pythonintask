# Задача 7. Вариант 20.
#  Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Titov I. V.
# 02.06.2016

import random

avtori = ("Кирилл", "Мефодий")

zagadka = random.choice(avtori)

predpologenie = input("Программа загадала одного из составителей славянской азбуки\nВаше предположение: ")

b = 1
schet = 1000

while b:
    if predpologenie == zagadka:
        print("Beeeeest", "\nСчёт - ", schet)
        b = 0
    else:
        print ("Неправильно\n")
        schet-=500
        predpologenie = input("Следующее предположение - ")

input("\n\nВведите ENTER для выхода")
