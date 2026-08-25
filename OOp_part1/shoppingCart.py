class product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class shoppingCart:

    def __init__(self):
        self.L = []

    def add_product(self,product):
        self.L.append(product)

    def calculate(self):
        total = 0
        for product in self.L:
            total+=product.price*product.quantity
        return total

    def display(self):
        for i in self.L:
            print(i.name,i.price,i.quantity)

product1 = product('apple',100,12)
product2 = product('banana',200,12)

cart = shoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.display()
print('Total',cart.calculate())