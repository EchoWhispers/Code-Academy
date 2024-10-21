class Bank_Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        return self.deposit_amount + self._balance

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self._balance < self.withdraw_amount:
            print(f"Not enough money in a bank account")

        else:
            self.withdraw_amount = withdraw_amount

    def check_balance(self):
        return self._balance + self.deposit_amount - self.withdraw_amount


bank = Bank_Account(800)


bank.deposit(150)
bank.withdraw(750)
print(bank.check_balance())


# class Bank_Account:
#     def __init__(self, balance):
#         self._balance = balance  # _balance is intended to be protected
#
#     def deposit(self, deposit_amount):
#         self._balance += deposit_amount  # Update balance after deposit
#         return self._balance
#
#     def withdraw(self, withdraw_amount):
#         if withdraw_amount > self._balance:
#             return "Insufficient funds"
#         self._balance -= withdraw_amount  # Update balance after withdrawal
#         return self._balance
#
#     def check_balance(self):
#         return self._balance
#
#
# # Example usage:
# bank = Bank_Account(800)
#
# bank.deposit(150)
# bank.withdraw(50)
# print(bank.check_balance())
