class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def deposite(self):
        amount = int(input('Enter deposite amount: '))
        if amount > 0:
            self.__balance = self.__balance+amount
            print('deposite successful: ')
        else:
            print('Invalid amount: ')

    def withdraw(self):
        withdraw_amount = int(input('Enter withdraw amount: '))
        if withdraw_amount > 0 and withdraw_amount <= self.__balance:
            self.__balance = self.__balance-withdraw_amount
            print('Withdraw successful: ')
        else:
            print('Invalid withdraw amount: ')

    def get_balance(self):
        return self.__balance

obj = BankAccount(10000)
obj.deposite()
obj.withdraw()
print(obj.get_balance())
