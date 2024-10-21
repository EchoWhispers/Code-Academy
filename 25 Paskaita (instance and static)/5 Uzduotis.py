class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary


    def give_raise(self, persentage):
        self.persetage = persentage


    def set_raise_amt(self, persentage):
        pass

    @staticmethod
    def standart_performance_index(score):
        pass


class Manager(Employee):

    subordinates = []
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def add_subordinate(self, emp):