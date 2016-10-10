#Задача 5. Вариант 11.
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из девяти оленей Санта Клауса.

#Козлов А.Д.
#14.03.2016
import random
first="Дэшер"
second="Дэнсер"
third="Прэнсер"
forth="Виксен"
fifth="Комет"
sixth="Кьюпид"
seventh="Дондер"
eight="Блитцен"
ninth="Рудольф"
print("Программа случайным образом выводит имя одного из 9 оленей Санты")
a=random.randint(1,9)
if(a==1):
	print(first)
elif (a==2):
	print(second)
elif (a==3):
	print(third)
elif (a==4):
	print(forth)
elif(a==5):
	print(fifth)
elif(a==6):
	print(sixth)
elif(a==7):
	print(seventh)
elif(a==8):
	print(eight)
elif (a==9):
	print(ninth)
input("\n\n\nНажмите Enter для завершения")
