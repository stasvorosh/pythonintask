#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, 
#чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, 
#если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, 
#отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Ермашов А.В., 26.05.2016
import random
schet = 10000
spisok = ("александр", "программа", "клавиатура", "руки", "голова", "студент", "информатика")
zagadannoe=random.choice(spisok)
vvod = zagadannoe
i=0
anagramma = ""
while zagadannoe:
	bykva = random.randrange(len(zagadannoe))
	anagramma+= zagadannoe[bykva]
	zagadannoe = zagadannoe[:bykva]+zagadannoe[(bykva+1):]
print("Анаграммы")
print("Загаданное слово: ", anagramma)
word = input ("Ваш ответ: ")
while (word != vvod):
	if(word == ""):
		print("Подсказка!",i+1,"буква: ",vvod[i],"!")
		i+=1
		schet-=2000
		word=input("Ваше слово: ")
		continue
	word=input("Неправильно. Попробуй еще раз: ")
	schet-=1000
	if schet <= 0:
		schet
		break
if word == vvod:
	print("\nПравильно! Это слово: ", vvod)
	print("Вы набрали",schet," очков!")
else:
	print("Вы проиграли, у вас 0 очков. Загаданное слово:",vvod)
input ("Нажмите ENTER для продолжения")
