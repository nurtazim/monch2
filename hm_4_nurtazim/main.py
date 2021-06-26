"""Импорт всех задач из Calculator1 """

from hm_4_nurtazim.homeworks import Calculator1
import random


"""Лист рандома из 100 чисел выделено 20 случайных чисел"""

def rand_list() :
    rand_list = []
    while len(rand_list) < 20:

        r = random.randint(1,100)
        if r not in rand_list :
            rand_list.append(r)
    return rand_list

"""Вывод одного числа из 20 случайных  чисел"""

random1=random.choice(list(rand_list()))
random2=random.choice(list(rand_list()))


"""Инициализация класса"""
class Calculator(Calculator1.Additions,Calculator1.Divisions,Calculator1.Substraction,Calculator1.Multiplication):

    """class Calculator():<-- можно было так но VAL1  начал светиться, а если добавить обьекты то не светилось , в любом случае  оба варианта работают """

    def division(val1,val2):
       print(Calculator1.Divisions.divisions(val1,val2))
       pass
    def addition(*val1,**val2):
       print(Calculator1.Additions.addisions(*val1,**val2))
       pass
    def multiplication(val1,val2):
       print(Calculator1.Multiplication.multiplicat(val1,val2))
    def substraction(val1,val2):
       print(Calculator1.Substraction.substract(val1,val2))
       pass


"""Показ всех операции из обьекта класса """

Calculator.division(val1=random1,val2=random2)
Calculator.multiplication(val1=random1,val2=random2)
Calculator.substraction(val1=random1,val2=random2)
Calculator.addition(val1=random1,val2=random2)


"""Бесконечное значение и сложение любых цифр"""

Calculator.addition(51,51,5,15,5,15,1,51,5,15,1,5)
