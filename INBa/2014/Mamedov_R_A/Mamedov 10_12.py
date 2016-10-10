# Задача 10, вариант 12

# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, 
# которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. 
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула",
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Мамедов Р.А.
# 10.05.2016

# Константа главного меню:
MENU = ("""
Главное меню:
   0. Выход.
   1. Добавить очки.
   2. Убрать очки.
У вас есть {} очка/-ов развития.
   """)
# Параметры героя в виде словаря:
attribute_points = 30
attributes = {"сила": 0,
             "ловкость": 0,
             "мудрость": 0,
             "здоровье": 0,
             }
# Константа - "меню параметров":
STATS_MENU = ("""
Ваши параметры:
    0. Выйти в предыдущее меню.
    1. Сила = {0}
    2. Ловкость = {1}
    3. Мудрость = {2}
    4. Здоровье = {3}
У вас {4} очка/-ов развития.
    """)
# Теперь сама программа.
# Предлагаем пользователю поработать с главным меню.
choise = ""
while choise != "0":
    print(MENU.format(attribute_points))
    # Просим пользователя выбрать нужный пункт.
    choise = input("Укажите нужный вам пункт меню: ")
        
    # Обрабатываем ввод пользователя.
    if choise == "0":
        print("Программа завершена") # Это выход из программы.
    elif choise == "1" or choise == "2":        
        # Предлагаем пользователю поработать с меню "выбора параметров".
        selected_attribute = ""            
        while selected_attribute != "0":
            # Это вывод на экран самого меню:
            print(STATS_MENU.format(attributes["сила"], attributes["ловкость"], attributes["мудрость"], attributes["здоровье"], attribute_points))
            selected_attribute = input("Введите номер параметра, для изменения или \"0\", для выхода: ")
            
            if selected_attribute == "1" or selected_attribute == "2" or selected_attribute == "3"\
                or selected_attribute == "4" or selected_attribute == "0":
                if selected_attribute == "0": # Возврат в предыдущее меню.
                    continue            
                # Принимаем значение выбранного пункта меню.    
                elif selected_attribute == "1":
                    alterable_attribute = "сила"
                elif selected_attribute == "2":
                    alterable_attribute = "ловкость"
                elif selected_attribute == "3":
                    alterable_attribute = "мудрость"
                elif selected_attribute == "4":
                    alterable_attribute = "здоровье"
                else:
                    print("Пункта меню", str(selected_attribute), "не существует")
                    input("Нажмите Enter, для продолжения...")
                # Блок Увеличения Параметра.
                if choise == "1":                
                    change = int(input("Укажите на какое значение нужно увеличить {}: ".format(alterable_attribute)))
            
                    # Проверка на правильный ввод:                   
                    while change > attribute_points or change < 0:
                        print("Ваш запас очков равен - ", attribute_points)
                        print("Вы решили увеличить на {}!".format(change))
                        change = int(input("Укажите верное значение"))
                    # Теперь можно, изменить параметр.                               
                    attribute_points = attribute_points - change
                    attributes[alterable_attribute] += change
                # Блок Уменьшения Параметра.
                elif choise == "2":                
                    change = int(input("Укажите на какое значение нужно уменьшить {}: ".format(alterable_attribute)))
                    # Проверка на правильный ввод:
                    while change > attributes[alterable_attribute] or change < 0:
                        print("Параметр, который вы хотите уменьшить, равен {} очку/-ам ".format(alterable_attribute) )
                        print("Вы решили увеличить на {}!".format(change))
                        change = int(input("Укажите верное значение"))
                    # Теперь можно, уменьшить параметр.
                    attribute_points = attribute_points + change
                    attributes[alterable_attribute] -= change
            else:
                print("Пункта меню", str(selected_attribute), "не существует")
                input("Нажмите Enter, для продолжения...") 
            
    else:
        print("Пункта меню", str(choise), "не существует")
        input("Нажмите Enter, для продолжения...")   
    







