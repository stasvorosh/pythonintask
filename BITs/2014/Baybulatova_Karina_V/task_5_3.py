#Задача 5, Вариант 3
#Напишите программу, которая бы при запуске случайным образом отображала название одного из цветов радуги.

#Байбулатова К.В.
#19.03.2016


import random
a="Красный"
b="Оранжевый"
c="Желтый"
d="Зеленый"
e="Голубой"
f="Сигий"
g="Фиолетовый"
color=random.randint(1,7)
print("Программа случайным образом отображает название одного из цветов радуги")
if color==1:
	print(a)
elif color==2:
	print(b)
elif color==3:
	print(c)
elif color==4:
	print(d)
elif color==5:
	print(e)
elif color==6:
	print(f)
elif color==7:
	print(c)
input("Нажми Enter для выхода.")
