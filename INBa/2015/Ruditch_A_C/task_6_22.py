#Задача 6. Вариант 22
#Создайте игру, в которой компьютер загадывает имена двух братьев, легендарных основателей Рима, а игрок должен его угадать.

#Rudich A.C.
#30.03.2016
print('Угадайте имя одного из двух братьев, легендарных основателей Рима, которую загадал компьютер')
import random
a = random.choice(['Ромул', 'Рем'])
b = input('Ваш ответ: ')

b=''
while a !=b : 
	print ('Вы не угадали')
	b = input('Ваш ответ: ')

print ('Вы угадали: ' + a + ' - ' + b)
input('\nНажмите Enter для выхода')