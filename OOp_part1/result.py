class result:

    def __init__(self,name,rollNum,english,math):
        self.name = name
        self.rollNum = rollNum
        self.english = english
        self.math = math
        

    def cal_total(self):
        self.total = self.math+self.english
        return self.total

    def percentage(self):
        return (self.total/200)*100

    def Pass(self):
        if self.english >= 40 and self.math >= 40:
            return 'Pass'
        return 'Fail'

obj1 = result('akash',12,80,70)
obj2 = result('parkash',40,60,50)

print('Name is : ',obj1.name)
print('Roll Num is :',obj1.rollNum)
print('total marks is: ',obj1.cal_total())
print('Percentage is: ',obj1.percentage())
print('Result is: ',obj1.Pass())
print()
print('Name is : ',obj2.name)
print('Roll Num is :',obj2.rollNum)
print('total marks is: ',obj2.cal_total())
print('Percentage is: ',obj2.percentage())
print('Result is: ',obj2.Pass())