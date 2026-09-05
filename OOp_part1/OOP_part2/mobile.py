class mobile:

    def __init__(self,brand,price):
        self.brand = brand
        self.__price = price

    def display(self):
        return self.brand

    def get_price(self):
        return self.__price

    def change_Price(self,new_price):
        self.__price = new_price

obj = mobile('samsung',500000)
print(obj.display())
print(obj.get_price())
obj.change_Price(600000)
print(obj.get_price())