class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'Запуск отрисовки'


class Pen:
    def draw(self):
        return f'Рисуем ручкой'


class Pencil:
    def draw(self):
        return f'Рисуем карандашом'


class Handle:
    def draw(self):
        return f'Рисуем маркером'


p = Pen()
print(p.draw())
p_1 = Pencil()
print(p_1.draw())
h = Handle()
print(h.draw())