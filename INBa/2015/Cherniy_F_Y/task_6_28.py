# Задача 6. Вариант 28.
# Создайте игру, в которой компьютер загадывает название одного из шести континентов Земли, а игрок должен его угадать.

# Cherniy F. Y.
# 27.03.2016

import random

print("Компьютер загадал название одного из шести континентов Земли, а Вы должны его угадать.\n")

continents = ('Евразия','Африка','Северная Америка','Южная Америка','Австралия','Антарктида')
continent = random.randint(0,5)
x = 0

#print (continents[0]\n,continents[1]\n,continents[2]\n,continents[3]\n,continents[4]\n,continents[5])

while(x != 6):
	print(continents[x])
	x += 1

answer = input("\nВведите название континента: ")

while(answer != continents[continent]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите название континента: ")
	
print("Верно, Вы победили!")

input("\nДля выхода нажмите Enter.")