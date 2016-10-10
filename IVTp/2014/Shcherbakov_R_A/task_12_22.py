# Задача 12. Вариант 22.
# Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python
# гл. 6).

# Щербаков Р.А.
# 22.05.2016

print("""
Добро пожаловать на игру крестики нолики 
чтобы сделать ход введите число от 0 до 8
	 
	          0 | 1 | 2
	          ---------
	          3 | 4 | 5
	          ---------
	          6 | 7 | 8""")
doska=["-","-","-","-","-","-","-","-","-"]
bol=True
wins=False
schet=0
def disp(doska):
     print("\n\t"+doska[0]+" | "+doska[1]+" | "+doska[2]+"\n\t---------"+
	 "\n\t"+doska[3]+" | "+doska[4]+" | "+doska[5]+"\n\t---------"+
	 "\n\t"+doska[6]+" | "+doska[7]+" | "+doska[8]+"\n\t---------")
def win(doska):
     twin=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
     for row in twin:
	     if doska[row[0]]==doska[row[1]]==doska[row[2]]!="-":
		     return True
while wins!=True:
     if(schet==5):
         break
     if(bol):
         n1=input("\nХод игрока 1: ")
         if(doska[int(n1)]=="-"):
             doska[int(n1)]="X"
             disp(doska)
             bol=False
             wins=win(doska)
             schet+=1
         else:
	         print("Занято")
     else:
         n2=input("\nХод игрока 2: ")
         if(doska[int(n2)]=="-"):
             doska[int(n2)]="O"
             disp(doska)
             bol=True
             wins=win(doska)
         else:
	         print("Занято")
if(wins and bol):
     print("Победил игрок 2")
elif(wins and not bol):
     print("Победил игрок 1")
else:
     print("Ничья")
input("Ok")