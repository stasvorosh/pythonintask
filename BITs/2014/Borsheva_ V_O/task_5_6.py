#задача5,вариант 6
#программа случайным образом отображает название одного из двух спутников Марса.

#Борщёва В.О
#14.03.2016

import random
Phobos='фобос'
Deimos='деймос'
satellite=random.randint(1,2)
if satellite==1:
    print(Phobos)
elif satellite==2:
    print(Deimos)
    input("нажмите enter для выхода")
