class System:

    def __init__(self,name,accountNum,balance):
        self.name = name
        self.accountNum = accountNum
        self.balance = balance

    def deposite(self):
        amount = int(input('Enter deposite amount: '))
        self.balance = self.balance+amount
        print('deposite amount is: ',amount)

    def withdraw(self):
        amount = int(input('Enter amount for withdraw:'))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print('withdrawal successful:',amount)
        else:
            print('amount is high: ')

    def display(self):
        print('Balance is :',self.balance)

obj = System('akash',123,1000)
print('balance',obj.display())
print('deposte',obj.deposite())