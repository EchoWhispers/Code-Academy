from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, currency, value):
        self.currency = currency
        self.value = value

    def get_value(self):
        return self.value
    def get_currency(self):
        return self.currency
    @abstractmethod
    def convert_to_currency(self, target_currency, conversion_rate):
        pass
class Cash(Money):
    def __init__(self,currency, value, denomination):
        super().__init__(self,currency, value, denomination)
        self.denomination = denomination
    def convert_to_currency(self, target_currency, conversion_rate):


# from abc import ABC, abstractmethod
#
# class Money(ABC):
#     def __init__(self, currency: str, value: float):
#         self.currency = currency
#         self.value = value
#
#     def get_value(self) -> float:
#         return self.value
#
#     def get_currency(self) -> str:
#         return self.currency
#
#     @abstractmethod
#     def convert_to_currency(self, target_currency: str, conversion_rate: Dict[str, float]) -> None:
#         pass
#
# class Cash(Money):
#     def __init__(self, currency: str, value: float, denomination: int):
#         super().__init__(currency, value)
#         self.denomination = denomination
#
#     def convert_to_currency(self, target_currency: str, conversion_rate: Dict[str, float]) -> None:
#         self.value = round(self.value * conversion_rate[self.currency] * conversion_rate[target_currency], 2)
#         self.currency = target_currency
#         for _ in range(int(self.value / self.denomination)):
#             self.value -= self.denomination
#
# class Card(Money):
#     def __init__(self, currency: str, value: float, credit_limit: float):
#         super().__init__(currency, value)
#         self.credit_limit = credit_limit
#
#     def convert_to_currency(self, target_currency: str, conversion_rate: Dict[str, float]) -> None:
#         self.value = round(
#             min(self.value, self.credit_limit) * conversion_rate[self.currency] * conversion_rate[
#                 target_currency], 2)
#         self.currency = target_currency
