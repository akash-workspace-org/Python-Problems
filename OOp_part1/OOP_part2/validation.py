class validation:

    def __init__(self,salary):
        self.__salary = salary

    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print('salary is invalid: ')

obj = validation(1000)
obj.set_salary(-100)