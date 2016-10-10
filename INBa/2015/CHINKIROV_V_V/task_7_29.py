# Задача 7. Вариант 15.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее 
# количество баллов за меньшее количество попыток.

# Чинкиров В.В. ИНБ-ДБ1
# 11.05.2016, 11.05.16
balls=7
import random
print("Создайте игру, в которой компьютер загадывает имя одного из двенадцати апостолов, а игрок должен его угадать.")
print("У вас 7 попыток")
choice = random.randint(1,13)
if choice == 1:
    choice="Валек"
elif choice == 2: 
    choice="Петр"
elif choice == 3: 
	choice="Андрей"
elif choice == 4: 
	choice="Иоанн"
elif choice == 5: 
	choice="Иаков"
elif choice == 6: 
	choice="Филипп"
elif choice == 7: 
	choice="Варфоломей"
elif choice == 8: 
	choice="Матфей"
elif choice == 9: 
	choice="Фома"
elif choice == 10: 
	choice="Фадей"
elif choice == 11: 
	choice="Иуда"
elif choice == 12: 
	choice="Иаков Алфеев"
elif choice == 13:
        choice="Cимон Канонит"
print("Угадайте одного из аппостолов: ")
otvet = input("\nВведите имя аппостала: ")
while(otvet != choice):
    print("\nНеправильно. Попробуй еще раз")
    balls=balls-1
    otvet = input("\nВведите имя аппостала: ")

print("Правильно! Имя аппостала",choice,"!")
if balls>0: 
    print("Вы набрали ",ochki," очков! Поздравляем!")
elif balls<=0:
    print("У вас 0 очков. Вы проиграли. Попробуйте еще.")
input("Нажмите ENTER для продолжения")
