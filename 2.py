class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width


    def calculation(self):
        weight = self._lenght * self._width * 25 * 5 / 1000
        return f'{weight} тонн'



r = Road(5000, 15)
print(r.calculation())







