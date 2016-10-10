#Задача 8. Вариант 8.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
 
#Ionova A.K.
#27.05.16

import random
ball = 10
slova = ("земля", "огонь", "вода", "небо")
slovo = random.choice(slova)
bukvi = len(slovo)
print ("Я загадал некоторое слово. В нём ", bukvi, " букв(/-ы)." )
ls = list(slovo)
random.shuffle(ls)
anagram = ls
i = 0
print(anagram)
otvet = ""
while(otvet!=slovo):
	print("Назовёте слово сразу?(да/нет)")
	otvet = str(input())
	if (otvet == str("да")):
		print("Введите свой ответ: ")
		otvet = str(input())
		if (otvet == slovo):
			if (ball < 0):
				ball == 0
			print("Поздравляю, Вы победили. Ваш счет: ", str(ball))
	else:
		print("Хотите взять подсказку(да/нет)")
		otvet = str(input())
		if (otvet == str("да")):
			print("Подсказка!", i+1, "буква: ", slovo[i])
			ball -= 2
		else:
			print("\nПопытка - не пытка.")
			break
input ("\nНажмите Enter для выхода.")