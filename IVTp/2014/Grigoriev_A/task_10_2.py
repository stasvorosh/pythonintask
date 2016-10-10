#Задача 10. Вариант 2.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

#Григорьев А.О.
#11.04.2016
import random

class solution:
    def main(self):
        self.max_stat=30
        print('''
             ***Генератор персонажей***
       У вас  есть 30 параметров, которые вы можете
распределить между: силой, здоровьем, интелектом и ловкостью.
              Давайте начнем!
    (Для того что бы завершить просто введите "Конец")
''')
        self.sila=0
        self.zdorov=0
        self.um=0
        self.lovkost=0      
        while True:
            self.printhar()
            print("Осталось очков распределения: ", self.max_stat)
            if (self.max_stat<0):
                print("НЕПРЕДВИДЕННАЯ БАГА")
            vvod=input("\nВведите характеристику которую хотите изменить: ")
            if vvod=="Сила":
                self.strenghth(self.max_stat,self.sila)
                continue
            if vvod=="Здоровье":
                self.health(self.max_stat,self.zdorov)
                continue
            if vvod=="Интеллект":
                self.mind(self.max_stat,self.um)
                continue
            if vvod=="Ловкость":
                self.agility(self.max_stat,self.um)
                continue
            if vvod=="Конец":
                print("\n\n\n!!!Конечные!!!")
                self.printhar()
                input("\n\n\nНажмите Enter для закрытия окна")
                return

        
    def strenghth(self,max_stat,sila):
        while True:
            print("\nЧтобы вернуться к выбору характеристики введите \"Назад\"\nОчков силы ", self.sila)
            whattodo=input("Что хотите сделать(Добавить/Отнять):")
            if(whattodo=="Назад"):
                return
            if(whattodo=="Добавить"):
                dobav=int(input("Сколько очков силы хотите добавить? "))
                if self.max_stat<dobav:
                    print("Не хватает очков распределения.")
                    continue
                self.sila+=dobav
                self.max_stat-=dobav
                print("Осталось очков распределения: ", self.max_stat)
                continue
            elif(whattodo=="Отнять"):
                if self.sila==0:
                    print("Невозможно изменить т.к.  сила равна 0")
                    continue
                otnat=int(input("Сколько очков силы хотите отнять? "))
                if self.max_stat<otnat:
                    print("Не хватает очков распределения.")
                    continue
                if (otnat>self.sila):
                    print("Невозможно столько отнять.")
                    continue
                self.sila-=otnat
                self.max_stat+=otnat
                print("Осталось очков распределения: ", self.max_stat)
                continue

    def health(self,max_stat,zdorov):
        while True:
            print("\nЧтобы вернуться к выбору характеристики введите \"Назад\"\nОчков здоровья ", self.zdorov)
            whattodo=input("Что хотите сделать(Добавить/Отнять):")
            if(whattodo=="Назад"):
                return
            if(whattodo=="Добавить"):
                dobav=int(input("Сколько очков здоровья хотите добавить? "))
                if self.max_stat<dobav:
                    print("Не хватает очков распределения.")
                    continue
                self.zdorov+=dobav
                self.max_stat-=dobav
                print("осталось очков распределения: ", self.max_stat)
                continue
            elif(whattodo=="Отнять"):
                if self.zdorov==0:
                    print("Невозможно изменить т.к. здоровье равно 0")
                    continue
                otnat=int(input("Сколько очков здоровья хотите отнять? "))
                if (otnat>self.zdorov):
                    print("Невозможно столько отнять.")
                    continue
                self.zdorov-=otnat
                self.max_stat+=otnat
                print("Осталось очков распределения: ", self.max_stat)
                continue

    def mind(self,max_stat,mind):
            while True:
                print("\nЧтобы вернуться к выбору характеристики введите \"Назад\"\nОчков интеллекта ", self.um)
                whattodo=input("Что хотите сделать(Добавить/Отнять):")
                if(whattodo=="Назад"):
                    return
                if(whattodo=="Добавить"):
                    dobav=int(input("Сколько очков интеллекта хотите добавить? "))
                    if self.max_stat<dobav:
                        print("Не хватает очков распределения.")
                        continue
                    self.um+=dobav
                    self.max_stat-=dobav
                    print("осталось очков распределения: ", self.max_stat)
                    continue
                elif(whattodo=="Отнять"):
                    if self.um==0:
                        print("Невозможно изменить т.к. интеллект равен 0")
                        continue
                    otnat=int(input("Сколько очков интеллекта хотите отнять? "))
                    if self.max_stat<otnat:
                        print("Не хватает очков распределения.")
                        continue
                    if (otnat>self.um):
                        print("Невозможно столько отнять.")
                        continue
                    self.um-=otnat
                    self.max_stat+=otnat
                    print("Осталось очков распределения: ", self.max_stat)
                    continue
    
    def agility(self,max_stat,lovkost):
            while True:
                print("\nЧтобы вернуться к выбору характеристики введите \"Назад\"\nОчков ловкости ", self.lovkost)
                whattodo=input("Что хотите сделать(Добавить/Отнять):")
                if(whattodo=="Назад"):
                    return
                if(whattodo=="Добавить"):
                    dobav=int(input("Сколько очков ловкости хотите добавить? "))
                    if self.max_stat<dobav:
                        print("Не хватает очков распределения.")
                        continue
                    self.lovkost+=dobav
                    self.max_stat-=dobav
                    print("осталось очков распределения: ", self.max_stat)
                    continue
                elif(whattodo=="Отнять"):
                    if self.lovkost==0:
                        print("Невозможно изменить т.к. ловкость равна 0")
                        continue
                    otnat=int(input("Сколько очков ловкости хотите отнять? "))
                    if self.max_stat<otnat:
                        print("Не хватает очков распределения.")
                        continue
                    if (otnat>self.lovkost):
                        print("Невозможно столько отнять.")
                        continue
                    self.lovkost-=otnat
                    self.max_stat+=otnat
                    print("Осталось очков распределения: ", self.max_stat)
                    continue




            

    def printhar(self):
        print("\nХарактеристики персонажа:\nСила = ",self.sila,"\nИнтеллект = ",self.um,"\nЗдоровье = ", self.zdorov,"\nЛовкость = ",self.lovkost)
        return

obj = solution()
obj.main()


#strength, healh, mind, agility
