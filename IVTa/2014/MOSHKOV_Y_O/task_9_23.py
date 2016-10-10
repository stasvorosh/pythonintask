# Задача 9. Вариант 23
# Создайте игру, в которой компьютер выбирает какое-либо слово,
# а игрок должен его отгадать. Компьютер сообщает игроку, сколько
# букв в слове, и дает пять попыток узнать, есть ли какая-либо буква
# в слове, причем программа может отвечать только "Да" и "Нет".
# Вслед за тем игрок должен попробовать отгадать слово.

# Moshkov Y. O.
# 12.05.2016

import random
TESTS = 5
words = ["delete", "applet", "chain", 
"store", "memory", "application", "standard"]
number = random.randint(0, 6)
word = words[number].lower()

letter = ''
print("Отгадайте слово из", len(word), "букв")
print("У вас есть", TESTS, "попыток угадать буквы из слова.")
for i in range (TESTS):
        letter = input("Введите букву: ")
        if letter in word:
                print("Данная буква есть в слове")
answer = input("\nТеперь введите слово: ")
if word == answer:
        print("Вы выиграли!")
else:
        print("Неправильно. Вы проиграли.")
        print("Правильный ответ:", word)
input("Нажмите Enter для выхода")
