# Задача 5. Вариант 50.
#Напишите программу, которая бы при запуске случайным образом отображала название одной их четырех карточных мастей 
#стандартной французской колоды.
# Напишите программу, которая бы при запуске случайным образом отображала название
# одного из четырех животных, встреченных Колобком в лесу.

# Alekseev I.S.
# 15.05.2016

import random

print("Программа случайным образом отображает название одной из четырех мастей.")

mast = random.randint(1,4)

print('\nМасть называется', end=' ')

if mast == 1 :
    print('черви')
elif mast == 2 :
    print('крести') 
elif mast == 3 :
    print('буби') 
else :
    print('пики')


input("\n\nНажмите Enter для выхода.")
