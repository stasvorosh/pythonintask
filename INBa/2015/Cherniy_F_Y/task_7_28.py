# Задача 7. Вариант 28.
# 1-50. Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Cherniy F. Y.
# 28.03.2016

import random

print("Компьютер загадал название одного из шести континентов Земли, а Вы должны его угадать.\n")

continents = ('Евразия','Африка','Северная Америка','Южная Америка','Австралия','Антарктида')
continent = random.randint(0,5)
x = 0
i = 0
score = 0

#print (continents[0]\n,continents[1]\n,continents[2]\n,continents[3]\n,continents[4]\n,continents[5])

while(x != 6):
	print(continents[x])
	x += 1

answer = input("\nВведите название континента: ")

while(answer != continents[continent]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите название континента: ")
    i += 1

if i == 0:
	score = 10
	
elif 0<i<6:
	score = 10 - i*2
	
else:
	score = 0

print("Верно, Вы победили!")
print("Число попыток: "+str(i))
print("Вы заработали "+str(score)+" баллов")

input("\nДля выхода нажмите Enter.")
