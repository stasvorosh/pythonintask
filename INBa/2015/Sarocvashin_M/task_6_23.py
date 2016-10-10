# Задача 6. Вариант 23
#Создайте игру, в которой компьютер загадывает название одного из семи дней недели, а игрок должен его угадать.

# Сароквашин Максим 
# 12.05.2016


import random

print("Компьютер загадал название одного из семи дней недели, а Вы должны его угадать.\n")

days = ('Понедельник','Вторник','Срела','Четверг','Пятница','Суббота','Воскресенье',)
day= random.randint(0,6)
x = 0


while(x != 7):
	print(days[x])
	x += 1

answer = input("\nВведите день: ")

while(answer != days[day]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\nВведите название дня: ")
	
print("Верно, Вы победили!")

input("\nДля выхода нажмите Enter.")
