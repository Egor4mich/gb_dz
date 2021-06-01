import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running():
        time_to_sleep = [7, 2, 5]
        for color, sleep_time in zip(TrafficLight.__color, time_to_sleep):
            print(color)
            time.sleep(sleep_time)
