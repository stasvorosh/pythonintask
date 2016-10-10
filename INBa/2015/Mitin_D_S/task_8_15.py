# Задача 8. Вариант 15.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. 
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. 
# Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Mitin D.S.
# 19.04.2016, 11:08

import random
ochki = 500000
slova = ("питон", "программирование", "компьютер", "университет", "россия", "безопасность", "информатика")
zagadka=random.choice(slova)
proverka = zagadka
i=0
jumble = ""
while zagadka:
	bykva = random.randrange(len(zagadka))
	jumble += zagadka[bykva]
	zagadka = zagadka[:bykva] + zagadka[(bykva+1):]
print("Вы попали в передачу 'Анаграммы'")
print("Загаданное слово: ", jumble)
slovo = input ("Ваш ответ: ")
while (slovo != proverka):
	if(slovo == "не знаю"):
		print(i,"буква: ",proverka[i])
		i+=1
	if ochki <= 0:
		break
	slovo=input("Неправильно. Попробуй еще раз: ")
	ochki-=50000
if slovo == proverka: 
	print("\nПравильно! Это слово: ", proverka)
	print("Вы набрали",ochki," очков! Поздравляем!")
else: 
	print("К сожалению, у вас 0 очков, и вы проиграли :( Загаданное слово:",proverka)
input ("Нажмите ENTER для продолжения")
