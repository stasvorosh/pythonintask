# Задача 8. Вариант 9.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. 
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Кодзоков М.М., 26.05.2016

import random
points = 1000
words =("мурат","зачет","ргсу","алексей","солнце","настроение","работа")
choice=random.choice(words)
check = choice
i=0
anagramma = ""
while choice:
	symbol = random.randrange(len(choice))
	anagramma += choice[symbol]
	choice = choice[:symbol] + choice[(symbol+1):]
print("Привет. Давай сыграем в Анаграммы!")
print("Я загадал слово: ", anagramma)
vibor = input ("Твое слово: ")
while (vibor != check):
	if(vibor == ""):
		print(i,"буква: ",check[i])
		i+=1
	if points <= 0:
		break
	vibor=input("Неправильно. Попробуй еще раз: ")
	points-=100
if vibor == check: 
	print("\nПравильно! Это слово:", check)
	print("Ты набрал",points,"очков! Молодец!")
else: 
	print("К сожалению, у тебя 0 очков, и ты проиграл. Загаданное слово:",check)
input ("Нажмите ENTER для продолжения")
