# Задача 6. Вариант 23
# Создайте игру, в которой компьютер загадывает название одного из 
# семи чудес света, а игрок должен его угадать.

# Burmistrov V. D.
# 31.03.2016

import random
wonder = ["Пирамида Хеопса", "Висячие сады Семирамиды", "Храм Артемиды в Эфесе", "Статуя Зевса в Олимпии", "Мавзолей в Галикарнасе", "Колосс Родосский", "Александрийский маяк"]
number = random.randint(0, 6)
a = wonder[number]

inputA = input("Угадайте одно из семи чудес света: ")
if (inputA.lower() == a.lower()):
	out = "\nВы угадали."
else:
	out = "\nВы проиграли. Правильный ответ - " + a + "."
out += " Нажмите Enter для выхода."
input(out)