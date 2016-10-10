# Задача 5. Вариант 8.

# Напишите программу, которая бы при запуске случайным
# образом отображала название одного из семи дней недели.

# Egorov V.E.
# 02.03.2016

import random

print("Сейчас будет")

week_numbers = random.randint(1,7)

if week_numbers == 1 :
    week = 'Понедельник'
elif week_numbers == 2 :
    week = 'Вторник'
elif week_numbers == 3 :
    week = 'Среда' 
elif week_numbers == 4 :
    week = 'Четверг'
elif week_numbers == 5 :
    week = 'Пятница'
elif week_numbers == 6 :
    week = 'Суббота' 
elif week_numbers == 7 :
	week = 'Воскресенье'
print(' И это:', week)

input("\n\nНажмите Enter для выхода.")
