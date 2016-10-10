# Задача 6. Вариант 20.
# Создайте игру, в которой компьютер загадывает имя одного из семи друзей Белоснежки,
#, а игрок должен их угадать

# Titov I. V.
# 02.06.2016

import random

avtori = ("Вася ", "Петя ", "Вова ","Коля ","Русик ","Ваня ","Миша")
zagadka = random.choice(avtori)
predpologenie = input("Программа загадала одного из гномов друзей Белоснежки\nВаше предположение: ")
if predpologenie.lower() == zagadka.lower():
    print("Beeeeest")
else:
    print ("Неправильно\nПравильный ответ - " + zagadka)

input("\n\nВведите ENTER для выхода")
