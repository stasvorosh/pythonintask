#Задача 10. Вариант 10.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

#Кишуков Назир
#25.05.2016

POINT = 30 
ochki = 30 
person = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"} 
points = 0 
choice = None
while choice != 0: 
    print("""
1 - Добавить очков к характеристике
2 - Уменьшить очков характеристики
3 - Просмотр характеристик
0 - Выход
""")
   choice = int(input("Выберите пункт: "))
   if choice == 1:
       print("Пожалуйста, введите характеристику. ", len(person), "характеристики:")
        for item in person:
            print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Такой характеристики не существует: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество очков. Вам доступно", ochki, "очков")
            points = int(input("\n:"))
            while points > ochki or points < 0: 
                print("Вы не можете сделать столько очков. Доступно", ochki, "свободных очков")
                points = int(input("\n:"))
        person[char] = points
        print(points, "очков было добавлено к", char)
        ochki -= points 
    elif choice == 2:
        print("Пожалуйста, введите имя характеристики. Доступно изменение для: ")
        for item in person:
            if int(person[item]) > 0:
                print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Такой характеристики не существует: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество очков. Доступно", person[char], "очков:")
            points = int(input("\n:"))
            while points > int(person[char]) or points < 0:
                print("Вы не можете сделать столько очков. Доступно", person[char], "очков")
                points = int(input("\n:"))
        person[char] = points
        print(points, "очков было удалено")
        ochki= points
    elif choice == 3:
        print("\nХарактеристики Вашего героя")
        for item in person:
            print(item, "\t\t", person[item])
        
    elif choice == 0:
        print("Ваш персонаж создан!")
    else:
        print("В меню нет такого пункта")
input("Нажмите ENTER для продолжения") 
