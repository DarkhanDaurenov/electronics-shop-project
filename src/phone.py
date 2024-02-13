from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, count):
        super().__init__(name, price, quantity)
        self._count = count


    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self._count})"


    @property
    def number_of_sim(self):
        return self._count


    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError(":Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            return value












