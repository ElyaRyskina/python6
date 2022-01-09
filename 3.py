class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': int(wage), 'бонус': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
        return f'{self.name} {self.surname}'


    def get_total_income(self):
        return self._income['оклад'] + self._income['бонус']


w = Position('Иван', 'Иванов', 'менеджер', 15000, 10000)
print(w.name)
print(w._income)
print(w.position)
print(w.get_full_name())
print(w.get_total_income())