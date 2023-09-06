import threading
import time
import random


def car_race(car_name, distance):
    traveled = 0
    print(f'Thread = {threading.current_thread()}')
    while traveled < distance:
        speed = random.randint(1, 5)
        traveled += speed
        print(f"{car_name} проїхав {traveled} км")
        time.sleep(1)

    print(f"{car_name} фінішував!")
    return '1'


def main():
    car1 = threading.Thread(target=car_race, args=("Автомобіль 1", 10))
    car2 = threading.Thread(target=car_race, args=("Автомобіль 2", 10))
    car3 = threading.Thread(target=car_race, args=("Автомобіль 3", 10))

    car1.start()
    car2.start()
    car3.start()

    print('Гонка розпочалась')
    print(f'After start threads active count = {threading.active_count()}')

    car1.join()
    car2.join()
    car3.join()

    print("Гонка завершена!")


if __name__ == "__main__":
    print(threading.main_thread())
    print(f'Before main active count = {threading.active_count()}')
    main()
    print(f'After main active count = {threading.active_count()}')
