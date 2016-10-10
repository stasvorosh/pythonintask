#Задача 10.Вариант 46
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть
#предоставлено 30 пунктов, которые можно распределить между
#четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость.
#Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего
#"пула", но и возвращать их туда из характеристик, которым он решил присвоить
#другие значения.

#Gryadin V.D.
from tkinter import *

class Application(Frame):
    """ Создание класса """ 
    def __init__(self, window):
        """ Инициализация рамки и нанесение записей """
        super(Application, self).__init__(window)    
        self.grid()
        self.totalcoast = 30
        self.totalPOWER = 5
        self.totalHP = 5
        self.totalMIND = 5
        self.totalAG = 5
       
             
        self.lbl = Label(self,text = "Распределите очки и создайте персонажа: 30")
        self.lbl.grid(row = 0,column = 1)
        """ СИЛА """
        self.lbl1 = Label(self,text = "Сила:")
        self.lbl1.grid(row = 1,column = 1,sticky = W)
        self.lblp = Label(self,text = "5")
        self.lblp.grid(row = 1,column = 2)
        """ЗДОРОВЬЕ"""
        self.lbl2 = Label(self,text = "Здоровье:")
        self.lbl2.grid(row = 2,column = 1,sticky = W)
        self.lblhp = Label(self,text = "5")
        self.lblhp.grid(row = 2,column = 2)
        """ Мудрость """
        self.lbl3 = Label(self,text = "Мудрость:")
        self.lbl3.grid(row = 3,column = 1,sticky = W)
        self.lblm = Label(self,text = "5")
        self.lblm.grid(row = 3,column = 2)
        """ ЛОВКОСТЬ """
        self.lbl4 = Label(self,text = "Ловкость:")
        self.lbl4.grid(row = 4,column = 1,sticky = W)
        self.lbla = Label(self,text = "5")
        self.lbla.grid(row = 4,column =2)

        self.create_POWER()
        self.create_HP()
        self.create_MIND()
        self.create_AG()

                   #КНОПКИ СИЛЫ
        
    def create_POWER(self):
        self.bttn1 = Button(self)
        self.bttn1["text"] = "-"
        self.bttn1["command"] = self.MinusPower
        self.bttn1.grid(row = 1,column = 3)
        
        self.bttn2 = Button(self)
        self.bttn2["text"] = "+"
        self.bttn2["command"] = self.PlusPower
        self.bttn2.grid(row = 1,column = 4)
        
    def MinusPower(self):
        if self.totalPOWER!=0 and self.totalcoast!=30:
            self.totalPOWER -=1
            self.totalcoast +=1
            self.lbl = Label(self,text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblp = Label(self,text = str(self.totalPOWER))
            self.lblp.grid(row = 1,column = 2)        
    def PlusPower(self):
        if self.totalPOWER!=30 and self.totalcoast!=0 :
            self.totalPOWER +=1
            self.totalcoast -=1
            self.lbl = Label(self, text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblp = Label(self,text = str(self.totalPOWER))
            self.lblp.grid(row = 1,column = 2)

                 #КНОПКИ ЗДОРОВЬЯ

    def create_HP(self):
        self.bttn3 = Button(self)
        self.bttn3["text"] = "-"
        self.bttn3["command"] = self.MinusHP
        self.bttn3.grid(row = 2,column = 3)
        
        self.bttn4 = Button(self)
        self.bttn4["text"] = "+"
        self.bttn4["command"] = self.PlusHP
        self.bttn4.grid(row = 2,column = 4)
        
    def MinusHP(self):
        if self.totalHP!=0 and self.totalcoast!=30:
            self.totalHP -=1
            self.totalcoast +=1
            self.lbl = Label(self,text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblhp = Label(self,text = str(self.totalHP))
            self.lblhp.grid(row = 2,column = 2)        
    def PlusHP(self):
        if self.totalHP!=30 and self.totalcoast!=0 :
            self.totalHP +=1
            self.totalcoast -=1
            self.lbl = Label(self, text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblhp = Label(self,text = str(self.totalHP))
            self.lblhp.grid(row = 2,column = 2)

                  #КНОПКИ МУДРОСТИ

    def create_MIND(self):
        self.bttn5 = Button(self)
        self.bttn5["text"] = "-"
        self.bttn5["command"] = self.MinusMIND
        self.bttn5.grid(row = 3,column = 3)
        
        self.bttn6 = Button(self)
        self.bttn6["text"] = "+"
        self.bttn6["command"] = self.PlusMIND
        self.bttn6.grid(row = 3,column = 4)
        
    def MinusMIND(self):
        if self.totalMIND!=0 and self.totalcoast!=30:
            self.totalMIND -=1
            self.totalcoast +=1
            self.lbl = Label(self,text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblm = Label(self,text = str(self.totalMIND))
            self.lblm.grid(row = 3,column = 2)        
    def PlusMIND(self):
        if self.totalMIND!=30 and self.totalcoast!=0 :
            self.totalMIND +=1
            self.totalcoast -=1
            self.lbl = Label(self, text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lblm = Label(self,text = str(self.totalMIND))
            self.lblm.grid(row = 3,column = 2)

                   #КНОПКИ ЛОВКОСТИ

    def create_AG(self):
        self.bttn7 = Button(self)
        self.bttn7["text"] = "-"
        self.bttn7["command"] = self.MinusAG
        self.bttn7.grid(row = 4,column = 3)
        
        self.bttn8 = Button(self)
        self.bttn8["text"] = "+"
        self.bttn8["command"] = self.PlusAG
        self.bttn8.grid(row = 4,column = 4)
        
    def MinusAG(self):
        if self.totalAG!=0 and self.totalcoast!=30:
            self.totalAG -=1
            self.totalcoast +=1
            self.lbl = Label(self,text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lbla = Label(self,text = str(self.totalAG))
            self.lbla.grid(row = 4,column = 2)        
    def PlusAG(self):
        if self.totalAG!=30 and self.totalcoast!=0 :
            self.totalAG +=1
            self.totalcoast -=1
            self.lbl = Label(self, text = "Распределите очки и создайте персонажа:" + str(self.totalcoast))
            self.lbl.grid(row = 0,column = 1)
            self.lbla = Label(self,text = str(self.totalAG))
            self.lbla.grid(row = 4,column = 2)
        
# Основа
root = Tk()
root.title("Генератор персонажа для RPG")
root.geometry("320x200")
app = Application(root)
root.mainloop()

