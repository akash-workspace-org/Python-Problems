class setterGetter:

    def __init__(self,name,age,balance):
        self.name = name
        self.__age = age
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance = new_balance


obj = setterGetter('akash',balance=10000,age=20)

print(obj.get_balance())
obj.set_balance(2000)
print(obj.get_balance())