#Задача №5, Вариант 2
#Напишите программу, которая бы при запуске случайным образом отображала название одного из цветов радуги.

#Григорьев А.О.
#23.05.2016

import random 
a="красный"
b="оранжевый"
с="желтый"
d="зеленый"
e="голубой"
q="синий"
w="фиолетовый"
country=random.randint(1,7)
print("Программа случайным образом отображает название одного из цветов радуги")
if country==1:
	print(a)
elif country==2:
	print(b)
elif country==3:
	print(c)
elif country==7:
	print(d)
elif country==4:
	print(e)
elif country==5:
	print(q)
elif country==6:
	print(w)
input("Нажмите Enter для выхода.")