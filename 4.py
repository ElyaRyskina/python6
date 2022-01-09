class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'Машина поехала'


    def stop(self):
        return f'Машина остановилась'


    def turn(self, direction):
        return f'Машина повернула {direction}'


    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость!'
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость!'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, )



c = Car(70, 'red', 'Mazda', False)
print(c.go())
print(c.turn('налево'))
print(c.show_speed())
t_c = TownCar(50, 'red', 'Mazda', False)
print(t_c.go())
print(t_c.show_speed())
w_c = WorkCar(50, 'blue', 'Audi', False)
print(w_c.show_speed())
