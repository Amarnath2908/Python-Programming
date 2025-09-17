class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount
    def withdraw(self,amount):
        if (self.__balance >= amount):
            self.__balance = self.__balance - amount
        else:
            print("Insufficient balance") 
    def get_balance(self):
        print(f"The current balance is {self.__balance}")

d = BankAccount(10000)
d.deposit(1000)
d.withdraw(8000)
d.get_balance()




