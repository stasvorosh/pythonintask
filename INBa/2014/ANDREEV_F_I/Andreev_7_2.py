# Задача 7, Вариант 2 
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Андреев Ф.И.
# 25.05.2016

import random
print ('Отгадайте название одного из двенадцати созвездий, входящих в зодиакальный круг ')
def get_random_sozvdezdie():
   sozvdezdies = ("Овен","Телец","Близнецы","Рак","Лев","Дева","Весы","Скорпион","Стрелец","Козерог","Водолей","Рыбы")
   return random.choice(sozvdezdies)
sozvdezdie = get_random_sozvdezdie()
user_sozvdezdie = input('Введите ваш вариант: ')
ball = 9
while sozvdezdie.lower() != user_sozvdezdie.lower() and ball >1:
    ball -= 2
    print('У вас остлось', ball, 'баллов', 'Попробуйте ещё раз')
    user_sozvdezdie = input('Введите ваш вариант: ')
if ball > 1:
   print("Да вы отгдали!"'У вас остлось', ball)
else:
    print('Баллы закончились, а вы не угадали собор ')
input ('Нажмите Enter для выхода')





