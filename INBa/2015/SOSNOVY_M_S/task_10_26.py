POINT = 30 
ochki = 30 
person = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"} 
points = 0 
choice = None
while choice != 0: 
    print("""
0 - Выход
1 - Добавить пункты к характеристике
2 - Уменьшить пункты характеристики
3 - Просмотр характеристик
""")
    choice = int(input("Выбор пункта меню: "))
    if choice == 1:
        print("Пожалуйста, введите характеристику. ", len(person), "характеристики:")
        for item in person:
            print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, вы не в WoW: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов. У вас", ochki, "свободных пунктов")
            points = int(input("\n:"))
            while points > ochki or points < 0: 
                print("Вы не можете назначить такое количество пунктов", "Доступно", ochki, "свободных пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было добавлено к", char)
        ochki -= points 
    elif choice == 2:
        print("Пожалуйста, введите имя характеристики.", "Доступно изменение для: ")
        for item in person:
            if int(person[item]) > 0:
                print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, вы не в WoW: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов. Доступно", person[char], "пунктов:")
            points = int(input("\n:"))
            while points > int(person[char]) or points < 0:
                print("Невозможно удалить такое количество пунктов. Доступно", person[char], "пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было удалено")
        ochki += points
    elif choice == 3:
        print("\nХарактеристики Вашего героя")
        for item in person:
            print(item, "\t\t", person[item])
        
    elif choice == 0:
        print("BB")
    elif choice == 100500:
	    ochki += 99999999
	    print ("Вы  ввели чит код на 99999999 поинтов")
    else:
        print("В меню нет такого пункта")
