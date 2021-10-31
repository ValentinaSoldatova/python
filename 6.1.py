import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('Светофор включен')

        self.__color = 'red'
        print(f'Горит цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Горит цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Горит цвет: {self.__color}')
        time.sleep(5)

        while True:
            self.running()


tr_light = TrafficLight()
print(tr_light.running())