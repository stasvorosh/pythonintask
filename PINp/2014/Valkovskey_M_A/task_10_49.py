# Задача 10. Вариант 49.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
#Valkovskey M.A.
from operator import add, sub

character = {'name'      :    ' ',
             'power'     :      0,
             'health'    :      0,
             'knowledge' :      0,
             'speed'     :      0}

cons = 30

def info(character, rep=True):
  print('\nСила:\t\t', character['power'],
        '\nЗдоровье:\t', character['health'],
        '\nМудрость:\t', character['knowledge'],
        '\nЛовкость:\t', character['speed'],
        '\nОсталось', cons, 'баллов\n')
  if cons == 0 and rep:
    print("Введите 'конец' чтобы закончить\n")

character['name'] = input('Дайте имя вашему герою: ').capitalize()

print(
'\nХорошо, теперь опишите героя', character['name'],
'''
Героя можно развить в четырех направлениях:
Сила, Здоровье, Мудрость и Ловкость
У вас есть 30 очков, распределите их
Для этого вводите команды типа 'сила + 10' или 'ловкость - 5'
''')

while True:
  user = input('> ').lower().split()

  if len(user) != 3:
    if user[0] == 'конец':
      break
    print('Неправильная команда')
    continue

  what, how, much = None, None, 0

  if user[0] == 'сила':
    what = 'power'
  elif user[0] == 'здоровье':
    what = 'health'
  elif user[0] == 'мудрость':
    what = 'knowledge'
  elif user[0] == 'ловкость':
    what = 'speed'
  else:
    print('Неизвестная команда:', user[0])
    continue

  if user[1] == '+':
    how = add
  elif user[1] == '-':
    how = sub
  else:
    print('Неизвестный оператор:', user[1])
    continue

  try:
    much = int(user[2])
  except:
    print('Неизвестное число:', user[2])
    continue

  while True:
    abil = character[what]
    value = how(abil, much)
    diff = abil - value
    if value < 0 or (cons + diff) < 0:
      much =  much - 1
      continue
    break

  cons += abil - value
  character[what] = value

  info(character)

print('\nГерой', character['name'], 'готов у бою!')
info(character, rep=False)

input('Нажмите ENTER...')
