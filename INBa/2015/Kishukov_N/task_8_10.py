#Задача 8. Вариант 10.
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.#Чинкиров Валентин Владимирович 
#20.05.2016
#Кишуков Назир

import random
score = 10
words = ("Нальчик", "Кабардино-Балкарская Республика", "Ирина", "Аслан") 
word = random.choice(words)
letters = len(word)
print ("Я загадал некоторые слова связаные со мной. В нём ", letters, " букв(/-ы)." )
ls = list(word)
random.shuffle(ls)
anagram = ls
i = 0
print(anagram)
answer = ""
while(answer!=word):
	print("Назовёте слово сразу?(да/нет)")
	answer = str(input())
	if (answer == str("да")):
		print("Введите свой ответ: ")
		answer = str(input())
		if (answer == word):
			if (score < 0):
				score == 0
			print("Красавчик, Ты Грек!! Ваш счет: ", str(score))
	else:
		print("Хочешь  подсказку(да/нет)")
		answer = str(input())
		if (answer == str("да")):
			print("Подсказка!", i+1, "буква: ", word[i])
			score -= 2
		else:
			print("\nОПА!ОПА!!!")
			break
input ("\nНажмите Enter для выхода.")
