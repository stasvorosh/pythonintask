# Задача 10
# Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.

# Denisenko A. N.
# 02.06.2016

def print_skills ():
    global skills
    global znacheniya
    for i in range(5):
        print (skills[i],znacheniya[i])

def increase_skill ():
    global skills
    global znacheniya
    userSkill = int (input ("Куда накинем очков?\nСила - 1, здоровье - 2, мудрость - 3, ловксоть - 4\n"))
    while userSkill not in range (1,5):
        userSkill = int (input ("ОШИБОЧНЫЙ ВВОД! Попробуйте заново "))
    userNumber = int (input ("Сколько хотите накинуть? "))
    while userNumber <= 0 or userNumber > znacheniya[0] :
        userNumber = int (input ("ОШИБОЧНЫЙ ВВОД! Попробуйте заново "))
    znacheniya[userSkill] += userNumber
    znacheniya[0] -= userNumber
    print_skills()

def reduce_skill ():
    global skills
    global znacheniya
    userSkill = int (input ("Откуда заберём очки?\nСила - 1, здоровье - 2, мудрость - 3, ловксоть - 4\n"))
    while userSkill not in range (1,5) or znacheniya[userSkill] == 0:
        userSkill = int (input ("ОШИБОЧНЫЙ ВВОД! Попробуйте заново "))
    userNumber = int (input ("Сколько хотите отнять? "))
    while userNumber <= 0 or userNumber > znacheniya[userSkill] :
        userNumber = int (input ("ОШИБОЧНЫЙ ВВОД! Попробуйте заново "))
    znacheniya[userSkill] -= userNumber
    znacheniya[0] += userNumber
    print_skills()
    

skills = ("Осталось очков - ",'Сила ','Здоровье ','Мудрость ','Ловксоть ')
znacheniya = [30, 0 , 0 , 0 , 0]

print ("\tЭтому миру нужен новый герой!!!\n\n")


userDecision = 10
print_skills()
while userDecision != 1:
     userDecision = int (input ("Ваши действия? 1 - закончить разработку Генриха, 2 - увеличить какой-нибудь скилл, 3 - уменьшить какой-нибудь скилл\n"))
     if userDecision == 2:
         increase_skill()
     if userDecision == 3:
         reduce_skill()
     print()    
         
input("\n\nДля выхода нажмите ENTER")
