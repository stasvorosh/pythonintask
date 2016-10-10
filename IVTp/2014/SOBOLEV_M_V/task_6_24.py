import random
loshadi = ['Гнедая','Рыжая','Серая','Вороная']
otvet = input('')
otvet = otvet.lower()
otvet = otvet.capitalize()
if otvet == random.choice(loshadi):
	print('Верно!')
elif:
	print('Попробуйте еще раз!')
input()
