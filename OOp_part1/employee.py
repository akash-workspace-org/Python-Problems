class employee:

    def __init__(self,name,salary,dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def bonus(self):
        return self.salary*10/100+self.salary


obj = employee('akash',5000,'medical')
print('Salary after bonus is: ',obj.bonus())