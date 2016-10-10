# Задача 5. Вариант 11.
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из девяти оленей Санта Клауса. 
 
# Kurchatov N. V.
# 11.04.2016

import random
x=random.randint(1,9)
if x==1:
	name="Дэшер"
elif x==2:
	name = "Дэнсер"
elif x==3:
	name = "Прэнсер"
elif x==4:
	name = "Виксен"
elif x==5:
	name = "Комет"
elif x==6:
	name = "Кьюпид"
elif x==7:
	name = "Дондер"
elif x==8:
	name = "Блитцен"
elif x==9:
	name = "Рудольф"	
	
print ("Имя одного из оленей Санты - "+name)
input("Нажмите Enter для выхода")