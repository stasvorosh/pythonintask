# Задача 5. Вариант 31.
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух братьев, создателей старославянской азбуки.

# Шемякин А.В.
# 24.5.16
creators = ["Кирилл", "Мефодий"] #список создателей
import random as random_number; #импорт оператора random
print ("Данная программа выводит имя одного из создателей старославянской азбуки в случайном порядке");
print (random_number.choice(creators)); #случайный выбор из списка
input ("Press Enter to exit");
