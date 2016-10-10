# Задача 9. Вариант 21.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Platonova O. A.
# 29.05.2016

import random
words=("кортежи","списки","словари","циклы","ветвление","работа","компьютер")
compword=random.choice(words)
live=5
letter=""
number=len(compword)
if 10<=number<=20 or number%10==0 or 5<=number%10<=9:
    ok=''
elif number%10==1:
    ok="а"
else:
    ok="ы"
print("Я загадал слово, угадайте его. В этом слове",number,"букв"+ok+".")
print("У вас",live,"попыток, чтобы угадать буквы")
while live>0:
    letter=input("Введите букву\n")
    if letter in list(compword):
        print("Да.")
        live=live-1
    else:
        print("Нет.")
        live=live-1
    if 10<=live<=20 or live%10==0 or 5<=live%10<=9:
        ok='ок'
    elif live%10==1:
        ok="а"
    else:
        ok="и"
    print("Осталось",live,"попыт"+ok)
if live==0:
    myword=input("А теперь вам пора угадать слово!")
    if myword==compword:
        print("Вы угадали слово")
    else:
        print("Вы не угадали слово")
input("Нажмите Enter для выхода.")