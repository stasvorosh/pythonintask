#Задача 10. Вариант 8.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

#Ionova A.K.
#27.05.16

points = 30 
character = {"Сила":"0","Здоровье":"0","Мудрость":"0","Ловкость":"0"} 
ochki = 0
menu = None
while menu != 0: 
    print("0 - Выход\n1 - Добавить пункты к характеристике\n2 - Уменьшить пункты характеристики\n3 - Просмотр характеристик")
    menu = int(input("Выберите пункт меню: "))
    if menu == 1:
        print("\nДоступно", len(character), "характеристики для увеличения пунктов:")
        for item in character:
            print(item)
        char = str(input("Введите характеристику: "))
        char = char.title()
        while char not in character:
            char = str(input("Такой характеристики нет, повторите ввод: "))
            char = char.title()
        else:
            print("У вас", points, "свободных пунктов.")
            ochki = int(input("Введите количество пунктов: "))
            while ochki > points or ochki < 0: 
                print("Вы не можете назначить такое количество пунктов.", "Доступно", points, "свободных пунктов.")
                ochki = int(input("Повторите ввод: "))
        character[char] = ochki
        print(ochki, "пунктов было добавлено к", char)
        points -= ochki 
    elif menu == 2:
        print("\nДоступно", len(character), "характеристики для уменьшения пунктов:")
        for item in character:
            print(item)
        char = str(input("Введите характеристику: "))
        char = char.title()
        while char not in character:
             char = str(input("Такой характеристики нет, повторите ввод: "))
             char = char.title()
        else:
            print("Доступно", character[char], "пунктов.")
            ochki = int(input("Введите количество пунктов: "))
            while ochki > int(character[char]) or ochki < 0:
                print("Невозможно удалить такое количество пунктов. Доступно", character[char], "пунктов.")
                ochki = int(input("Повторите ввод:"))
        character[char] = ochki
        print(shmoints, "пунктов было удалено.")
        points += ochki
    elif menu == 3:
        print("\nХарактеристики Вашего героя")
        for item in character:
            print(item, "\t\t", character[item])
    elif menu == 0:
        print("Закрываю генератор...")
input ("\nНажмите Enter для выхода.")