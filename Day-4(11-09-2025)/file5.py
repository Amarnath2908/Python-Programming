class Payment:
    def pay(self,amount):
        self.amount = amount
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} in cash.")
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using debit/credit cards.")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

pays = [CashPayment(),CardPayment(),UPIPayment()]
for p in pays:
    p.pay(1000)