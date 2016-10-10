import random
loshadi = ['Гнедая','Рыжая','Серая','Вороная']
bally = int(10)
for i in range (bally):
    otvet = str(input('Ваш вариант: '))
    if otvet == str(random.choice(loshadi)):
        print ('Все верно! Ваши баллы: '+str(bally)+' из 10')
        break
    else:
        bally = bally-1
        print('Попробуйте еще раз!')
print('Вы исчерпали все попытки!')
input()
