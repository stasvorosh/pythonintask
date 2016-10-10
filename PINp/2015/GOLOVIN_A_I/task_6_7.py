# Задача 6. Вариант 7.
# Создайте игру, в которой компьютер загадывает имя одного из двух сооснователей компании #Google, а игрок должен его угадать.

# Golovin A.I.
# 02.06.2016

import random

avtori = ("Ларри Пейдж", "Сергей Михайлович Брин")
zagadka = random.choice(avtori)
predpologenie = input("Программа загадала одного из основателей гугл\nВаше предположение: ")
if predpologenie.lower() == zagadka.lower():
    print("ХААААААААРООООООООШ")
else:
    print ("Неправильно\nПравильный ответ - " + zagadka)

input("\n\nВведите ENTER для выхода")
