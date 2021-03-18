import time
class TrafficLight:

   # __color = ''

    def running(self):

        self.__color = 'red'
        print(f'{self.__color}')
        time.sleep(7)
        self.__color = 'yellow'
        print(f'{self.__color}')
        time.sleep(2)
        self.__color = 'green'
        print(f'{self.__color}')

a = TrafficLight()
a.running()
