class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехал.'

    def stop(self):
        return f'\nАвтомобиль  {self.name} остановился.'


    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'


    def show_speed(self):
        return f'\nВаша скорость составляет {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nВаша скорость выше допустимой. Составляет{self.speed}'
        else:
            return f'Скорость автомобиля {self.name} в допустимом пределе'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше допустимой. Составляет{self.speed}'
        else:
            return f'Скорость автомобиля{self.name} в допустимом пределе'


class PoliceCar(Car):
    pass


town = TownCar('Land Rover', 70, ',белый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('направо'), town.stop())

sport = SportCar('AudiR8', 200, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('УАЗ', 40, 'черный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Kia', 110, 'синий', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())