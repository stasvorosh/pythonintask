# Задача 8. Вариант 49
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право
# на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие
# слово без подсказки, получали больше тех, кто запросил подсказку.

# Ametova M.M.
# 26.05.2016  

import random

def check(answer, tip):
        if (answer != tsym):
                print("Неверно.")
        elif (tip > 0):
                tip -= 1
                nlet = random.randrange(len(correct))
                print(nlet + 1, "буква:", correct[nlet])
                print("Подсказки:", tip)
        else:
                print("Подсказок больше нет...")
        return tip

allkeys = ("magic", "rainbow", "box", 
"house", "staff", "jungle", "flame")
key = allkeys[random.randint(0, 6)]
anagram = ""
correct = key
tip = 5
tsym = '0'
for i in range (len(key)):
        pos = random.randrange(len(key))
        anagram += key[pos]
        key = key[:pos] + key[pos+1:]
print("Анаграмма:", anagram)
print("Чтобы использовать подсказку введите 0.")
strtip = "Ваш ответ: "
answer = input(strtip)
while answer != correct:
        tip = check(answer, tip)
        print("Ещё попытка.")
        answer = input(strtip)
print("Победа!")
points = len(correct) + tip
print("Cчёт: ", points)
input("Нажмите Enter для выхода")
