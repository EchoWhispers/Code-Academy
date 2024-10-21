class Currency:
    def __init__(self, code, amount, exchange_rate):
        self.code = code
        self.amount = amount
        self.exchange_rate = exchange_rate

    def set_code(self, code):
        self.code = code
        return self

    def set_amount(self, amount):
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate):
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code, new_exchange_rate):
        self.new_code = new_code
        self.new_exchange_rate = new_exchange_rate
        self.code = new_code


        self.amount = (self.amount * self.exchange_rate) / self.new_exchange_rate
        self.exchange_rate = self.new_exchange_rate
        return self.amount

    def __str__(self):
        return f"Currency: {self.code}, Amount: {self.amount}"


c = Currency("EUR", 500, 1.6)
print(c.set_code("EUR").set_amount(200).set_exchange_rate(0.9))
c.convert("GBP", 0.8)
print(c)


