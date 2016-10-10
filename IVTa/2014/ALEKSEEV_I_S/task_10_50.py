# Задача 10. Вариант 50

# Напишите программу "Генератор персонажей" для игры.

# Пользователю должно быть предоставлено 30 пунктов,

# которые можно распределить между четырьмя характеристиками:

# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,

# чтобы пользователь мог не только брать эти пункты из общего "пула",

# но и возвращать их туда из характеристик, которым он решил присвоить

# другие значения.



# Alekseev I.S.

# 25.05.2016



print("Генератор персонажа.")

umenia = ["Сила", "Здоровье", "Ловкость", "Интеллект"]

naviky = dict.fromkeys(umenia, 0)

points = 20
print("Доступно очков распределения",points)

umenia_label = ["%s-%s" % (i+1, x) for i, x in enumerate(umenia)] + ["0 - exit"]

prompt = "Выберите умение %s: " % umenia_label

while points!=0:
    
	try:
        
		i = int(input(prompt))
    
	except ValueError:
        
		print("Неверное действие!")
        
		continue
   
	if len(umenia) < i < 0:
        
		print("Неверное действие!")
        
		continue
    
	if i == 0:
        
		break
    
	action = input("+/- :")
    
	if action not in "+-":
        
		print("Неверное действие!")
        
		continue
    
	umenia_name = umenia[i-1]
    
	if action == "+":
        
		naviky[umenia_name] += 1
        
		points -= 1
        
		print("\nОчков распределения",points)
    
	else:
        
		naviky[umenia_name] -= 1
        
		points += 1
        
		print("\nОчков распределения",points)
    
	print(naviky)
print("\nОчки распределения закончились")
