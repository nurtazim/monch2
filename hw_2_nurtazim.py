class Person:
    """ ОПИСАНИЕ УЧЕНИКА"""
    __total_persons = 0
    __this_year=2021
    __language = "spanish"
    def __init__(self,__name,__birth_year,**kwargs):
        self.__name=__name
        self.__birth_year=__birth_year
        if self.__birth_year > Person.__this_year:
            raise Exception("Ошибка выдачи")
        self.__language=kwargs.get("Language")
        Person.__total_persons+=1

    def get_language(self):
        return self.__language



    def is_adult(self):
        return self.__this_year-self.__birth_year>=18



    def get_age(self):
        return 2021-self.__birth_year


    def get_total_persons(cls):
        return cls.__total_persons

    def talk(self):
        print ("Hello Word")


    def name(self):
        return  self.__name

class Teacher(Person):
    """ОПИСАНИЕ УЧИТЕЛЯ"""



    def talk(self):
        print(f"Greetings, I'm your teacher {self._Person__name}")


    def teach(self):
        print(f"Lesson started by {self._Person__name}")
#
p1 = Person('Nurik', 1999,language='russian')
p2 = Person('Diana', 2000, language='english')
p3 = Person('Elina', 2005, language=' korean')
t1 = Teacher('Kutman', 2002, language='spanish')
t2 = Teacher('Daniiar', 2000, language='kyrgyz')
t3 = Teacher('Abai', 2005, language='italian ')

print(t1.get_language())
print(p2.is_adult())
print(p1.is_adult())
print(t2.get_age())
p1.talk()
t2.teach()
t1.talk()
t1.teach()

