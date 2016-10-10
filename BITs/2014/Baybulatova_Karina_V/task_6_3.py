#Задача 6, Вариант 3
#Создайте игру, в которой компьютер загадывает имя одной из семи птиц, доступных с первой версии игры Angry Birds, а игрок должен его угадать.

#Байбулатова К.В.
#19.03.2016

import random
Angry_Birds=('Ред', 'Чак', 'Джей', 'Бомб', 'Матильда', 'Cтелла', 'Майти')
name=random.randint(0,6)
rand=Angry_Birds[name]
print("Я загадал одного из семи птиц Angry Birds")
#print (rand)
answer=0
while (answer)!=(rand):
	answer=input("Введите одного из птиц Angry Birds:")
	if (answer)!=(rand):
		print ("Вы не угадали. Попробуйте снова.")
	elif (answer)==(rand):
		print ("Вы угадали.")
		break

input("Нажмите Enter для выхода.")
