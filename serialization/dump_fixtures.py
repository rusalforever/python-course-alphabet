import random
import uuid
from homework import Car, Garage, Cesar
from constants import TOWNS, CARS_TYPES, CARS_PRODUCER

if __name__ == "__main__":
    Car.__module__ = "homework"
    cesar_id = str(uuid.uuid4())

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

    sample_car = cesar.garages[0].cars[0]
    sample_garage = cesar.garages[0]
    sample_cesar = cesar

    print(sample_car)
    sample_car.change_number
    car_json = Car.dumps_json(sample_car)
    print(car_json)
    Car.dump_json(sample_car)
    Car.dump_pickle(sample_car)
    Car.dump_yaml(sample_car)
    sample_car = Car.loads_json(car_json)
    print(sample_car)
    sample_car = Car.load_json()
    print(type(sample_car))
    print(sample_car)

    sample_garage = cesar.garages[0]
    print(sample_garage)
    garage_json = Garage.dumps_json(sample_garage)
    print(garage_json)
    Garage.dump_json(sample_garage)
    Garage.dump_pickle(sample_garage)
    Garage.dump_yaml(sample_garage)
    sample_garage = Garage.loads_json(garage_json)
    print(sample_garage)
    sample_garage = Garage.load_json()
    print(sample_garage)
    print(type(sample_garage))

    print(sample_cesar)
    print(Cesar.dump_json(sample_cesar))
    Cesar.dump_json(sample_cesar)
    Cesar.dump_pickle(sample_cesar)
    Cesar.dump_yaml(sample_cesar)
    sample_cesar = Cesar.load_json()
    print(type(sample_cesar))
    print(sample_cesar)

    sample_car = cesar.garages[0].cars[0]
    print(cesar.garages[0])
    s = Car.to_dict(sample_car)
    print(s)
    Car.dump_yaml(sample_car)
    print((Car.dumps_yaml(sample_car)))
    s = Car.load_yaml()
    print(s)
    print(type(s))

    sample_garage = cesar.garages[0]
    s = Garage.to_dict(sample_garage)
    print(s)
    Garage.dump_yaml(sample_garage)
    print((Garage.dumps_yaml(sample_garage)))
    s = Garage.load_yaml()
    print(s)
    print(type(s))

    s = Cesar.to_dict(cesar)
    print(s)
    Cesar.dump_yaml(cesar)
    s = Cesar.load_yaml()
    print(s)
    s = Cesar.dumps_yaml(cesar)
    print(s)
    print(Cesar.loads_yaml(s))

    pickled_car = Car.dumps_pickle(sample_car)
    print(pickled_car)
    Car.dump_pickle(sample_car)
    print(Car.loads_pickle(pickled_car))
    print(Car.load_pickle())

    pickled_garage = Garage.dumps_pickle(sample_garage)
    print(pickled_garage)
    Garage.dump_pickle(sample_garage)
    print(Garage.loads_pickle(pickled_garage))
    print(Garage.load_pickle())

    pickled_cesar = Garage.dumps_pickle(cesar)
    print(pickled_cesar)
    Cesar.dump_pickle(cesar)
    print(Cesar.loads_pickle(pickled_cesar))
    print(Cesar.load_pickle())