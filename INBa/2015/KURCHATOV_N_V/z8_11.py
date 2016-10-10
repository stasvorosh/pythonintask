#Задача 8. Вариант 11.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

#Kurchatov N.V.
#23.05.2016

import random
score = 10
words = ("телефон", "школа", "ноутбук", "рапира", "инвокер")
word = random.choice(words)
l = len(word)
print ("В загаданном слове", l, " букв." )
anagram = list(word)
random.shuffle(anagram)

i = 0
print(anagram)
answer = ""
while(answer!=word):
	print("Вы назовете слово?(y/n)")
	answer = str(input())
	if (answer == str("y")):
		print("Ответ: ")
		answer = str(input())
		if (answer == word):
			if (score < 0):
				score == 0
			print("Вы угадали. Ваш счет: ", str(score))
	else:
		print("Хотите взять подсказку(y/n)")
		answer = str(input())
		if (answer == str("y")):
			print("Вы использовали подсказку, но у вас сгорело два очка.", i+1, "буква: ", word[i])
			score -= 2
			i+=1
		else:
			print("До свидания")
			break
input ("\nНажмите Enter для выхода.")