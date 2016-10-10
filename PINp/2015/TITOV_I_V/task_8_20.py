# Задача 8
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
#так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
#подсказку в том случае, если у него нет никаких предположений. Разработайте
#систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
#получали больше тех, кто запросил подсказку.


# Titov I. V.
# 02.06.2016

import random

WORDS = ("pyton", "анаграммы", "easy", "hard", "answer", "прикуриватель",
         )
PODSCAZKA = ("вот он ", "вот так получилось", "довольно просто ", "не просто ",
             "узнай как так то", "ну впринципе",
             )
nomer = random.randrange(len(WORDS))
word = WORDS[nomer]
correct = word[:]
schet = 1000


jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]


print(
"""
           Здравствуйте!
        
   Значит так, переставляете буквы - выигрываете, всё просто
   (уже сдаётесь? нажимай ENTER)
   (подсказка - "летоблизко")
"""
)
print("Вперёд го: ", jumble)

guess = input("\nВаш вариант: ")
while guess != correct and guess != "":

    if guess.lower() == "летоблизко":
        print (PODSCAZKA[nomer])
        schet-=500
    else:    
        print("Очень, не очень")
        
    guess = input("Новый вариант: ")
    
if guess == correct:
    print("100% попадание (случайно)\nСчёт - ",schet)
else:
    print("))))))Ну бывает...")

print("До встречи!")

input("\n\nНажмите ENTER для выхода")
