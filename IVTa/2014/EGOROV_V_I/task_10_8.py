# Задача 10. Вариант 8
'''
Напишите программу "Генератор персонажей" для игры.
Пользователю должно быть предоставлено 30 пунктов,
которые можно распределить между четырьмя характеристиками:
Сила, Здоровье, Мудрость и Ловкость.
Надо сделать так, чтобы пользователь мог не только брать
эти пункты из общего "пула", но и возвращать их туда
из характеристик, которым он решил присвоить другие значения.
'''
# Egorov V. I.
# 07.04.2016

from operator import add, sub
  
ch = {'power'     : 5,
      'health'    : 5,
      'knowledge' : 5,
      'agility'   : 5}


point = 10

def info(ch):
	print(  '\nСила:\t\t',   ch['power'],
        '\nЗдоровье:\t', ch['health'],
        '\nМудрость:\t', ch['knowledge'],
        '\nЛовкость:\t', ch['agility'],
        '\nОсталось очков: ', point)

info(ch)

while True:
	
	aa = input('> ').lower().split()
  
	if len(aa) != 2:
		print('Неправильная команда')
		continue

	shoose1, shoose2 = None, 0
	
	if aa[0] == 'сила':
		shoose1 = 'power'
	elif aa[0] == 'здоровье':
		shoose1 = 'health'
	elif aa[0] == 'мудрость':
		shoose1 = 'knowledge'
	elif aa[0] == 'ловкость':
		shoose1 = 'agility'
	else:
		print('Неизвестная команда:', aa[0])
		continue

	try:
		shoose2 = int(aa[1])
	except:
		print('Неизвестное число:', aa[1])
		continue
    
	while True:
		abil = ch[shoose1]
		value = shoose2
		if abil < 2 and value < 1:
			print('Достигнуто минимальное значение характеристики')
		elif (abil + value) < 1:
			print('Недопустимое значение характеристики')
		elif (point - value) < 0:
			print('Не хватает очков')
		else:
			dif = abil + value
			point += abil - dif
			ch[shoose1] = dif
		break
	
	info(ch)
	
	
    
input('Нажмите ENTER...')

