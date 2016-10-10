# Задача 6. Вариант 30.
'''
Создайте игру, в которой компьютер загадывает название
одного из двенадцати месяцев, а игрок должен его угадать.
'''
# Shchukin F.O.
# 20.03.2016

from random import choice

print('Угадайте один из 12 месяцев!')

months = tuple('Январь Февраль Март Апрель Май Июнь Июль\
         Август Сентябрь Октябрь Ноябрь Декабрь'.split())

months = [x.lower() for x in months]

right = choice(months)
trys = []

k = 1
while True:
    print('\n', k, 'попытка..')
    word = input('> ').lower()
    
    if right == word:
        print('Правильно! Это', right + '!')
        input('\nНамите Enter...')
        break
    
    if word not in months:
        print('Такого месяца нет')
        continue
    
    if word in trys:
        print('Вы уже пробовали', word)
        continue
    trys.append(word)
    
    k += 1
    if k == 4:
        print('Подсказка: последниие две буквы -', right[-2:])
        
    elif k == 6:
        r = months.index(right)
        print('Подсказка:', months[r-1], '...',
              months[r+1 if r < len(months)-1 else 0])
        