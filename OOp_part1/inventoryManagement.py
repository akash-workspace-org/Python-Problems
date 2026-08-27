class inventoryManagement:

    def __init__(self,item_id,item_name,price,quantity):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def add_stock(self):
        stock = int(input('Enter stock: '))
        self.quantity+=stock

    def sell_item(self):
        item = input('Enter item name would you buy: ')
        if self.item_name == item:
            qnty = int(input('Enter quantity woud you buy: '))
            if qnty <= self.quantity:
                self.quantity-= qnty
                print('Item sold: ')
                print('Quantity: ',self.quantity)
            else:
                print('itni quantity avalaible nai hai: ')
        else:
            print('Ye item avalaible nai hai: ')

    def cal_total(self):
        print(self.price*self.quantity)

    def display(self):
        print('Item id: ',self.item_id)
        print('Item: ',self.item_name)
        print('Price: ',self.price)
        print('Quantity: ',self.quantity)

class Manu:

    def __init__(self):
        self.items = []
    def add_item(self):
            item_id = int(input('Enter item id: '))
            item_name = input('Enter item name: ')
            price = int(input('Enter item price: '))
            quantity = int(input('Enter quantity: '))
            new_item = inventoryManagement(item_id,item_name,price,quantity)
            print(new_item)
            self.items.append(new_item)

    def sell__item(self):
        itm_id = int(input('Enter id: '))
        qnty = int(input('Enter qnatity: '))
        for i in self.items:
            if i.item_id == itm_id:
                if qnty <= i.quantity:
                    i.quantity-=qnty
                    print('item sold')
                    break
                else:
                    print('Not have enough: ')
                    break
        else:
            print('item not found: ')


    def display_all(self):
        for i in self.items:
            i.display()
            print()

    def expensive(self):
        total = self.items[0].price
        highest1 = self.items[0]
        for i in self.items:
            if i.price > total:
                total = i.price
                highest1 = i
        print('Expensive item is: ',highest1.item_name)

    def highest_stock(self):
            total = self.items[0].quantity
            highest2 = self.items[0]
            for i in self.items:
                if i.quantity > total:
                    total = i.quantity
                    highest2 = i
            print('It have highest stock: ',highest2.item_name)

    def cal_inventory(self):
        total = 0
        for i in self.items:
            total += i.price * i.quantity
        print('total value is:', total)

inventory = Manu()
print('Add items: ')
inventory.add_item()
inventory.add_item()
print()
inventory.expensive()
inventory.highest_stock()
print('Sell item: ')
inventory.sell__item()
inventory.cal_inventory()
inventory.display_all()

