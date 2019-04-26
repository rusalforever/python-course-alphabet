from constants import *
import uuid
import random

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Cesar:
    def __init__(self, name, garages=None, register_id=None):
        self.register_id = register_id if register_id else uuid.uuid4()
        self.garages = garages if garages is not None else []
        self.name = name

    def __repr__(self):
        return f"Cesar(name='{self.name}', garages='{self.garages}')"

    def garages_count(self):
        return len(self.garages)

    def сars_count(self):
        return sum(len(garage.cars) for garage in self.garages)

    def add_car(self, car, garage=None):

        def place_available(garage):
            return garage.places - len(garage.cars)

        garage = garage or max(self.garages, key=place_available) if self.garages else None
        if garage and place_available(garage) > 0:
            garage.add(car)
        else:
            print('No place available ', garage)

    def hit_hat(self):
        return sum(garage.hit_hat() for garage in self.garages)

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()


class Car:
    def __init__(self, car_type: CARS_TYPES, producer: CARS_PRODUCER, price, mileage):
        self.price = price
        self.car_type = car_type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def __repr__(self):
        return f"Car(car_type='{self.car_type}', producer='{self.producer}', price='{self.price}, mileage='{self.mileage}')"

    def change_number(self):
        self.number = uuid.uuid4()

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __lt__(self, other):
        return self.price < other.price


class Garage:
    def __init__(self, town: TOWNS, places: int, owner: uuid.UUID, cars=None):
        self.cars = cars if cars is not None else []
        self.town = town
        self.places = places
        self.owner = owner

    def add(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
        else:
            print('No place available ', self)

    def remove(self, car: Car):
        self.cars.remove(car)

    def hit_hat(self):
        return sum(car.price for car in self.cars)

    def __repr__(self):
        return f"Garage(town='{self.town}', places='{self.places}', owner='{self.owner}, cars='{self.cars}')"


if __name__ == "__main__":
    cesar_id = uuid.uuid4()

    garages = []
    for _ in range(2):
        garage = Garage(
            town=random.choice(TOWNS),
            places=5,
            owner=cesar_id
        )
        garages.append(garage)

    cesar = Cesar('cesar', garages, cesar_id)

    cars = []
    for _ in range(10):
        car = Car(
            car_type=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            price=round(random.uniform(1, 100000), 2),
            mileage=round(random.uniform(1, 100000), 2)
        )
        cesar.add_car(car, random.choice(garages))

    print(cesar)
    print(cesar.garages[0])
    print('hit_hat garages[0] =', cesar.garages[0].hit_hat())
    print(cesar.garages[1])
    print('hit_hat garages[1] =', cesar.garages[1].hit_hat())
    print('hit_hat cesar = ', cesar.hit_hat())
    cesar2 = Cesar('cesar2')
    print(cesar2)
    print('hit_hat cesar2 = ', cesar2.hit_hat())
    print('cesar > cesar2 ', cesar > cesar2)
    print('cesar.сars_count = ', cesar.сars_count())
    cesar.garages[0].remove(cesar.garages[0].cars[0])
    print('cesar.сars_count = ', cesar.сars_count())
