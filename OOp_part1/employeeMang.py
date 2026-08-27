class employeeMang:

    def __init__(self,name,id,salary,department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def bonus(self):
        a = self.salary + self.salary*10/100
        print('Salary after bonus',a)

    def information(self):
        print('Name: ',self.name)
        print('Employee id: ',self.id)
        print('Salary: ',self.salary)
        print('Department: ',self.department)

    def annual(self):
        b  = self.salary*12
        print('Annual salary is: ',b)

    def heighest_salary(self,obj1,obj2):
        if obj1.salary > obj2.salary:
            print('Akash have heighest salary',obj1.salary)
        else:
            print('sooraj have heighest salary',obj2.salary)


obj1 = employeeMang('akash',123,10000,'cs')
obj2 = employeeMang('sooraj',321,2000,'bba')

obj1.information()
print()
obj2.information()
print()
obj1.bonus()
obj2.bonus()
print()
obj1.annual()
obj2.annual()
print()
obj1.heighest_salary(obj1,obj2)