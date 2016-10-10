# Задача 10. Вариант 23
# Напишите программу "Генератор персонажей" для игры.
# Пользователю должно быть предоставлено 30 пунктов,
# которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость. Надо сделать так,
# чтобы пользователь мог не только брать эти пункты из общего "пула",
# но и возвращать их туда из характеристик, которым он решил присвоить
# другие значения.

# Moshkov Y. O.
# 15.05.2016

print("Генератор персонажа.")

class Character:
        def __init__(self, points):
                self.attrib = ("Сила", "Ловкость", "Здоровье", "Мудрость")
                self.values = [8, 8, 8, 8]
                self.ppool = points
        def update(self, chrt, num):
                print()
                for i in range (len(self.attrib)):
                        if chrt.capitalize() == self.attrib[i]:
                                self.ppool -= num
                                if self.ppool < 0:
                                        num += self.ppool
                                        self.ppool = 0
                                self.values[i] += num
                        print(self.attrib[i], end = ' : ')
                        print(self.values[i])
                print("\nОчки:", self.ppool)

pers = Character(30)
chrt, num = "some", 0
while chrt != "":
        pers.update(chrt, num)
        chrt = input("\nХарактеристика: ").strip()
        temp = input("Очки (\"-\" для уменьшения, Enter для выхода): ").strip()
        if len(temp):
                if temp.isdigit() or temp[0] == '-':
                        num = int(temp)
print("\nСоздание персонажа завершено...")

input("Нажмите Enter для выхода")
