# Задача 6. Вариант 8.

# Напишите программу, которая бы при запуске случайным
# образом загадывала название одного из семи дней недели.

# Egorov V.E.
# 02.03.2016

import random

print("Программа случайным образом загадывает название одного дней недели, а игрок должен его угадать.")

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


trial = 3
bonus = 3000

while bonus > 0 :
    answer = input('\nНазовите один из дней: ')
    if answer == week :
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else :
        print('\nВы не угадали!!!')
        if trial > 1 :
            print('Попробуйте еще раз.')
        else :
            print('Ваши очки кончились \nПравильный ответ: ', week)
        
    trial -= 1
    if trial <=0 :
    	trial = 0.5
    bonus -= int(trial * 800)
    if bonus<=0 :
    	bonus = 0
    print('\nВаши очки', bonus)
