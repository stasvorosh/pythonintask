# Задача 6, Вариант 2 
# Создайте игру, в которой компьютер загадывает название одного из двенадцати созвездий, входящих в зодиакальный круг, а игрок должен его угадать.

# Андреев Ф.И.
# 24.05.2016

import random
sozvezdies = random.randrange(12)
sozvezdie = ("Овен","Телец","Близнецы","Рак","Лев","Дева","Весы","Скорпион","Стрелец","Козерог","Водолей","Рыбы")
print ('Отгадайте название одного из двенадцати созвездий, входящих в зодиакальный круг ')
user_sozvezdie = input ('Введите Ваш вариант: ')
while user_sozvezdie.lower() != sozvezdie[sozvezdies].lower():
    user_chudo = input ('Вы не угадали,попробуйте ещё раз: ')
print ('Вы угадали!')
input ('Нажмите Enter для выхода')
