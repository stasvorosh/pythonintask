# -*- coding: UTF-8 -*-
# Задача 5. Вариант 15.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из двенадцати городов, входящих в Золотое кольцо России.

# Mochalov V. V.
# 08.03.2016

import random
x=random.randint(1, 12)
if x == 1:
 print ('Сергиев Посад')
elif x == 2:
 print ('Переславль-Залесский')
elif x == 3:
 print ('Ростов')
elif x == 4:
 print ('Ярославль')
elif x == 5:
 print ('Кострома')
elif x == 6:
 print ('Иваново')
elif x == 7:
 print ('Суздаль')
elif x == 8:
 print ('Владимир')
elif x == 9:
 print ('Углич')
elif x == 10:
 print ('Плёс')
elif x == 11:
 print ('Юрьев-Польский')
elif x == 12:
 print ('Тутаев')

input("\n\nНажмите Enter для выхода.")
