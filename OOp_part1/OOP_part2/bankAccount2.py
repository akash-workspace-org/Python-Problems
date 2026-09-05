class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.__balance = self.__balance+amount
            print('deposite successful: ')
        else:
            print('Invalid amount: ')

    def withdraw(self,withdraw_amount):
        if withdraw_amount > 0 and withdraw_amount <= self.__balance:
            self.__balance = self.__balance-withdraw_amount
            print('Withdraw successful: ')
        else:
            print('Invalid withdraw amount: ')

    def get_balance(self):
        return self.__balance

obj = BankAccount(10000)
obj.deposite(1000)
obj.withdraw(2000)
print(obj.get_balance())
