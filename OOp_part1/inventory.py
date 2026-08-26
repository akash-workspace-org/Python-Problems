class inventory:

    def __init__(self,item_name,price,quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def add_stock(self):
        qnty = int(input('Enter quantity of item: '))
        self.quantity += qnty

    def sell_stock(self):
            qnty = int(input('Enter quantity of stock would you buy: '))
            if qnty <= self.quantity:
                self.quantity -= qnty
                print('item sold: ')
                print(self.quantity)
            else:
                print('requirment jitna stock avalaible nai hai: ')

    def calc_value(self):
        print(self.price*self.quantity)

    def display(self):
        print('Item name: ',self.item_name)
        print('Item price: ',self.price)
        print('Quantity: ',self.quantity)

obj = inventory('apple',100,12)
obj.display()
obj.add_stock()
obj.display()
obj.sell_stock()
obj.calc_value()