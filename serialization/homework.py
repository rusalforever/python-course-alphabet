"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

import sys
import pickle
import uuid
import random
import json
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from constants import TOWNS, CARS_TYPES, CARS_PRODUCER


class GenericJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            pass
        cls = type(obj)
        result = {
            '__name__': cls.__name__,
            'data': obj.__dict__
        }
        return result


class GenericJSONDecoder(json.JSONDecoder):
    def decode(self, str_to_decode):
        result = super().decode(str_to_decode)
        return GenericJSONDecoder.instantiate_object(result)

    @staticmethod
    def instantiate_object(result):
        cls = result.get('__name__', '__name__') if isinstance(result, dict) else None
        if cls in ['Car', 'Garage', 'Cesar']:
            cls = getattr(sys.modules['__main__'], cls)
            result.pop('__name__')
            instance = cls.__new__(cls)
            data = {k: GenericJSONDecoder.instantiate_object(v) for k, v in result['data'].items()}
            instance.__dict__.update(data)
            return instance
        else:
            return result


class MyJSONAble:

    @classmethod
    def loads_json(cls, data):
        return json.loads(data, cls=GenericJSONDecoder)

    @classmethod
    def load_json(cls):
        with open(f"{cls.__name__}.json", 'r') as file:
            return json.load(file, cls=GenericJSONDecoder)

    @staticmethod
    def dumps_json(obj):
        return json.dumps(obj, cls=GenericJSONEncoder)

    @staticmethod
    def dump_json(obj):
        with open(f"{obj.__class__.__name__}.json", 'w') as file:
            json.dump(obj, file, indent=4, cls=GenericJSONEncoder)


class MyPickleAble:

    @staticmethod
    def dumps_pickle(obj):
        return pickle.dumps(obj)

    @staticmethod
    def dump_pickle(obj):
        with open(f"{obj.__class__.__name__}.pickle", 'wb') as file:
            pickle.dump(obj, file)

    @classmethod
    def loads_pickle(cls, obj):
        return pickle.loads(obj)

    @classmethod
    def load_pickle(cls):
        with open(f"{cls.__name__}.pickle", 'rb') as file:
            return pickle.load(file)


class MyYAMLAble:
    yaml = YAML()

    @classmethod
    def to_dump(cls, data, stream=None, **kw):
        if stream is None:
            stream = StringIO()
        cls.yaml.dump(data, stream, **kw)
        return stream.getvalue()

    @classmethod
    def dump_yaml(cls, data):
        data = cls.to_dict(data)
        filename = '{}.yaml'.format(cls.__name__)
        with open(filename, "w") as file:
            config = cls.yaml.dump(data, file)
        return config

    @classmethod
    def dumps_yaml(cls, data):
        data = cls.to_dict(data)
        return cls.to_dump(data)

    @classmethod
    def load_yaml(cls):
        filename = '{}.yaml'.format(cls.__name__)
        with open(filename, "r") as file:
            config = cls.yaml.load(file)
        return cls.instantiate_yaml(cls, cls.__name__, config[cls.__name__])

    @classmethod
    def loads_yaml(cls, data):
        cls.dumps_yaml(data)
        return cls.load_yaml()

    @staticmethod
    def instantiate_yaml(cls, ins_class_name, result):
        if ins_class_name in ['Car', 'Garage', 'Cesar']:
            if hasattr(result, "__dict__"):
                result = dict(result)
            ins_class = getattr(sys.modules['__main__'], ins_class_name)
            instance = ins_class.__new__(ins_class)
            data = {}
            for (k, v) in result.items():
                if isinstance(v, list):
                    ch_list = []
                    for obj in v:
                        (ch_key, ch_val) = obj.popitem()
                        ch_list.append(cls.instantiate_yaml(cls, ch_key, ch_val))
                    data[k] = ch_list
                else:
                    data[k] = v
            instance.__dict__.update(data)
            return instance

    @classmethod
    def to_dict(cls, obj):
        if isinstance(obj, dict):
            data = {}
            for (k, v) in obj.items():
                data[k] = cls.to_dict(v)
            return data
        elif hasattr(obj, "__iter__") and not isinstance(obj, str):
            return [cls.to_dict(v) for v in obj]
        elif hasattr(obj, "__dict__"):
            return {obj.__class__.__name__: cls.to_dict(obj.__dict__)}
        else:
            return obj


class Car(MyJSONAble, MyYAMLAble, MyPickleAble):
    def __init__(self, car_type: CARS_TYPES, producer: CARS_PRODUCER, price, mileage, number=None):
        self.car_type = car_type
        self.producer = producer
        self.price = price
        self.mileage = mileage
        self.number = number if number else str(uuid.uuid4())

    def __repr__(self):
        return f"Car(car_type='{self.car_type}', producer='{self.producer}', price='{self.price}, " \
            f"mileage='{self.mileage}', number='{str(self.number)}')"

    def change_number(self):
        self.number = str(uuid.uuid4())

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price > other.price


class Cesar(MyJSONAble, MyYAMLAble, MyPickleAble):
    def __init__(self, name, garages=None, register_id=None):
        self.register_id = register_id if register_id else str(uuid.uuid4())
        self.garages = garages if garages is not None else []
        self.name = name

    def __repr__(self):
        return f"Cesar(name='{self.name}', garages='{self.garages}')"

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
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

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()


class Garage(MyJSONAble, MyYAMLAble, MyPickleAble):
    def __init__(self, town: TOWNS, places: int, owner, cars=None):
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
    car_json = Car.dumps_json(sample_car)
    print(car_json)
    Car.dump_json(sample_car)
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
    sample_garage = Garage.loads_json(garage_json)
    print(sample_garage)
    sample_garage = Garage.load_json()
    print(sample_garage)
    print(type(sample_garage))

    print(sample_cesar)
    print(Cesar.dump_json(sample_cesar))
    Cesar.dump_json(sample_cesar)
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
