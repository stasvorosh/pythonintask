# Задача 5, Вариант 8

# Напишите программу, которая бы при запуске
# случайным образом отображала название одного
# из семи дней недели.

# Карамян Н.Г.
# 22.05.2016

input ("Жмак......\n")

import random

day = random.randint(1, 7)

if (day) == 1:
    print ("Понедельник")
elif (day) == 2:
    print ("Вторник")
elif (day) == 3:
    print ("Среда")
elif (day) == 4:
    print ("Четверг")
elif (day) == 5:
    print ("Пятница")
elif (day) == 6:
    print ("Суббота")
elif (day) == 7:
    print ("Воскресенье")


input ("\n\nЕщё раз!\n")


day = random.randrange(7)+1

if (day) == 1:
    print ("Понедельник")
elif (day) == 2:
    print ("Вторник")
elif (day) == 3:
    print ("Среда")
elif (day) == 4:
    print ("Четверг")
elif (day) == 5:
    print ("Пятница")
elif (day) == 6:
    print ("Суббота")
elif (day) == 7:
    input ("Вот и всё.")

input ("\n\nВот и всё.")
