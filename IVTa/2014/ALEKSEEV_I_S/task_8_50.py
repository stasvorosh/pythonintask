# Задача 8. Вариант 50
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право
# на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие
# слово без подсказки, получали больше тех, кто запросил подсказку.

# Alekseev I.S.
# 14.05.2016  

import random

def response(answer, tips):
        if (answer != "tip"):
                print("Неправильный ответ.")
        elif (tips >= 0):
                nlet = random.randrange(len(correct))
                print(nlet + 1, "буква слова:", correct[nlet])
                print("Ещё доступно подсказок:", tips)
        else:
                print("У вас закончились подсказки") 

words = ("python", "shell", "interpreter", 
"log", "java", "style", "float")
word = random.choice(words)
print("Игра \"Анаграммы\"")
anagram = ""
correct = word
tips = int(len(word) / 2) + 1
while word:
        pos = random.randrange(len(word))
        anagram += word[pos]
        word = word[:pos] + word[pos + 1:]
print("Ваша анаграмма:", anagram)
strtip = "Введите ответ или \"tip\", чтобы использовать подсказку: "
answer = input(strtip)
while answer != correct:
        tips -= 1
        response(answer, tips)
        print("Попробуйте ещё раз.")
        answer = input(strtip)
print("Вы выиграли!")
points = len(correct) + tips * 3
print("Ваш счёт: ", points)
input("Нажмите Enter для выхода")
