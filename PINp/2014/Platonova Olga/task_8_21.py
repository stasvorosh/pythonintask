# Задача 8. Вариант 21.
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Platonova O. A.
# 29.05.2016

import random
words=("кортежи","списки","словари","циклы","ветвление","работа","компьютер")
onegame="y"
while onegame=="y" or onegame=="д":
    compword=random.choice(words)
    correct=compword
    jumble=""
    hint=""
    point=100
    while compword:
        position=random.randrange(len(compword))
        jumble+=compword[position]
        compword=compword[:position]+compword[(position+1):]
    print(
    """
                     Добро пожаловать в игру 'Анаграммы'!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
             (Для выхода нажмите Enter, не вводя своей версии.)
    """
    )
    print("Попробуйте разгадать анаграмму:",jumble)
    guess=" "

    while guess!=correct and guess!="":
            guess=input('Попробуйте отгадать загаданное слово, если вы не значете, напишите "подсказка": ')
            if guess=="подсказка":
                    hint=(correct [:position+1])
                    print(hint)
                    point-=10
                    position+=1
            elif guess==correct:
                    print("Да, именно так! Вы отгадали\n")
                    print("Ваши баллы",point)
            elif guess!=correct:
                    print("Не отгадали, попробуйте еще раз ")
    print("Спасибо за игру.")
    onegame=input("Если хотите сыграть ещё раз, введите д или y")
input("\n\nНажмите Enter, чтобы выйти.")