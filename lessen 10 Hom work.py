
class Employee:
    emp_count=0
    work_rate=2
    def __init__( self,name,salary):
        self.name=name
        self.salary=salary
    def display_count (self):
        pass

    def display_employee(self):
        print('Имя имя сотрудника: {}. Зарплата: {}'.format(self.name, self.salary))


    def change_name(self,new_name ):
      self.name=new_name

    def change_salary(self,new_salary):
        self.salary=new_salary

    def get_total_salary(self):
        return self.salary
human1=Employee("nurtazim",500000000)
human1.display_employee()
human1.change_name("MR Nurtazim")
human1.change_salary(50000000000000000000000000000000)
human1.display_employee()