# Задача 7. Вариант 49.
# Разработайте систему начисления очков для задачи 6, 
# в соответствии с которой игрок получал бы большее 
# количество баллов за меньшее количество попыток.
# Ametova M.
# 20.05.2016

import random

print('Угадайте ранг!')

mans = tuple('''Генерал-фельдмаршал
Адмирал
Генерал-лейтенант
Генерал-майор
Статский советник
Полковник
Подполковник
Капитан
Штабс-капитан
Поручик
Подпоручик
Прапорщик'''.split('\n'))

for man in mans: print(man)

mans = [x.lower() for x in mans]

right = random.choice(mans)

score_unit = 5
score = score_unit * len(mans)

k = 1
while True:
    print('\n', k, 'попытка. У вас', score, 'очков.')
    word = input('Введите ранг: ').lower()
    
    if right == word:
        print('Правильно! Это', right + '!')
        print('Вы заработали', score, 'очков!')
        input('\nНамите Enter...')
        break
        
    if word not in mans:
        print('Такого ранга нет')
        continue
    
    score -= score_unit
    
    k += 1
    if k == 2:
        print('Подсказка: последниие две буквы -', right[-2:])
        
    elif k == 4:
        r = mans.index(right)
        print('Подсказка:', mans[r-1], '...',
              mans[r+1 if r < len(mans)-1 else 0])
        
