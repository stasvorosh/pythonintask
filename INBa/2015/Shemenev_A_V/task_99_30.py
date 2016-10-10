#Задача №8, Вариант 30
#Доработать игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка. 
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, 
#получали больше тех, кто запросил подсказку.

#Шеменев А.В.
#28.05.2016

import random
WORDS=("питон","карма","простая","задание","глупость","подстаканник")
word=random.choice(WORDS)
correct=word
jumble=""
hint=""
ball=100
while word:
	position=random.randrange(len(word))
	jumble+=word[position]
	word=word[:position]+word[(position+1):]

print(
"""
		Добро пожаловать в игру 'Анаграмма'!
	Вам требуется переставить буквы так, чтобы получилось осмысленное слово.
(Для выхода нажмите Enter, не вводя своей версии.)
"""
)
print ("Вот она,Анаграмма:", jumble)
guess=" "
while guess !=correct and guess!="":       
	guess=input("Какое было исходное слово?: ")
	if guess=="подсказка":
		hint= (correct[:position+1])
		print (hint)
		ball-=10
		position+=1
	elif guess==correct:
		print("Всё верно! Вы правы!\n")
		print ("Итог",ball)
	elif guess!=correct:
		print("Неверно, попробуй еще раз.")
print("Спасибо за игру.")
input("Нажмите Enter для выхода.")