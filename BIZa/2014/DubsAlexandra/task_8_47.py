# Задача 8. 
# Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Dubs A. E.
# 27.04.2016

import random

WORDS = ("питон","анаграмма", "простая", "сложная", "ответ", "подстаканник")

word = random.choice(WORDS)

correct = word

jumble = word
jumble = list(jumble)

for i in range(0,100):
	position1 = random.randint(0,len(jumble)-1)
	position2 = random.randint(0,len(jumble)-1)
	temp = jumble[position1]
	jumble[position1] = jumble[position2]
	jumble[position2] = temp

jumble = str(jumble)


	
print ("Добро пожаловать в игру 'Анаграммы'! \n Надо переставить буквы так, чтобы получилось осмысленное слово. \n <Для выхода нажмите Enter, не вводя своей версии.>")

print ("Вот анаграмма:" , jumble)

podskazka = input ("Если нужна подсказка, ответь 'Да' ")
if podskazka == 'Да' :
	print(word[0:2])

guess = input ("\n Попробуйте отгадать слово: ")

while guess != correct and guess != "" :
	print ("К сожалению, вы не правы.")
	guess = input ("Попробуйте отгадать исходное слово:")

	if guess == correct:
		print ("Да, именно так! Вы отгадали! \n")

print ("Спасибо за игру!")
input ("\n\n Нажмите Enter для выхода")