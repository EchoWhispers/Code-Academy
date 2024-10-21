class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        return f"You successfully deposited {self.amount} EUR"

    def withdraw(self, wamount):
        self.wamount = wamount
        self.balance -= wamount
        if self.balance < 0:
            return f"Insufficient amount"
        else:
            return f"You successfully withdraw {self.wamount} EUR"
    def display(self):
        return f"Your balance: {self.balance} EUR"

    @classmethod
    def from_balance(cls, balance):
        pass



bank = BankAccount(0)
print(bank.deposit(200))
print(bank.display())
print(bank.withdraw(50))
print(bank.display())