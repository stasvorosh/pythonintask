# Задача 10. Вариант 21.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Platonova O. A.
# 30.05.2016


print ("""
			       Добро пожаловать в "Генератор персонажей".
	У Вас есть 4 характеристики между которыми Вы можете аспределить 30 очков:
                1. Сила, 2. Здоровье, 3. Мудрость и 4. Ловкость.
 Вы можете названить любое количество очков из допустимых 30 для этих характристик!
	""")
strength=0
health=0
intelligence=0
agility=0
point=30
chislo=0
getit=''
while getit!='5':
    if strength<0 or health<0 or intelligence<0 or agility<0 or point>30:
        print("Ошибка")
        break
        #chislo=int(input("Напишите снова"))
    elif point==0:
        print("Вы распределили очки. Их распределение:\nСила:",strength,"\nЗдоровье:",health,"\nМудрость:",intelligence,"\nЛовкость:",agility)
        break
    print("Ваши очки:\nСила:",strength,"\nЗдоровье:",health,"\nМудрость:",intelligence,"\nЛовкость:",agility,"\nНераспределённые очки:",point)
    getit=input("Если хотите изменить Силу, то введите '1'. Если Здоровье, то введите '2'. Если  Мудрость, то '3'. Для Ловкости, введите '4'. Для выхода нажмите '5'\n")
    if getit=="1":
        chislo=int(input("На сколько хотите изменить?\n"))
        if (point-chislo >= 0) and (0<=strength+chislo<=30):
            strength+=chislo
            point-=chislo
        else:
            print('Недопустимое значение')
    elif getit=="2":
        chislo=int(input("На сколько хотите изменить?\n"))
        if (point-chislo >= 0) and (0<=health+chislo<=30):
            health+=chislo
            point-=chislo
        else:
            print('Недопустимое значение')
    elif getit=="3":
        chislo=int(input("На сколько хотите изменить?\n"))
        if (point - chislo >= 0) and (0 <= intelligence + chislo <= 30):
            intelligence+=chislo
            point-=chislo
        else:
            print('Недопустимое значение')
    elif getit=="4":
        chislo=int(input("На сколько хотите изменить?\n"))
        if (point - chislo >= 0) and (0 <= agility + chislo <= 30):
            agility+=chislo
            point-=chislo
        else:
            print('Недопустимое значение')

input("Нажмите Enter для выхода.")