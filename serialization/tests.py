import os
import pickle
import unittest
import homework
from copy import deepcopy

from homework import Car, Garage, Cesar

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = os.path.join(PROJECT_PATH, "fixtures")


class BaseTestCases:
    __test__ = False

    def test_dumps_pickle(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.pickle")
        with open(file_name, 'rb') as file:
            expected_res = file.read()
        expected_res = pickle.loads(expected_res)
        test_res = pickle.loads(self.component.dumps_pickle(self.component))
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_dump_pickle(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.pickle")
        with open(file_name, 'rb') as file:
            expected_res = pickle.loads(file.read())
        test_file = file_name + '_test'
        self.component.dump_pickle(self.component, test_file)
        with open(test_file, 'rb') as file:
            test_res = pickle.loads(file.read())
        # os.remove(test_file)
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_load_pickle(self):
        expected_res = self.component
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.pickle") + '_test'
        test_res = self.component.load_pickle(file_name)
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_loads_pickle(self):
        expected_res = self.component
        test_res = self.component.loads_pickle(self.component.dumps_pickle(self.component))
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_dumps_yaml(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.yaml")
        with open(file_name, 'r') as file:
            expected_res = file.read()
        expected_res = expected_res.translate({ord(i): None for i in ' \t\n\r'})
        test_res = self.component.dumps_yaml(self.component).translate({ord(i): None for i in ' \t\n\r'})
        self.assertEqual(expected_res, test_res)

    def test_dump_yaml(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.yaml")
        with open(file_name, 'r') as file:
            expected_res = file.read()
        expected_res = expected_res.translate({ord(i): None for i in ' \t\n\r'})
        test_file = file_name + '_test'
        self.component.dump_yaml(self.component, test_file)
        with open(test_file, 'r') as file:
            test_res = file.read().translate({ord(i): None for i in ' \t\n\r'})
        # os.remove(test_file)
        self.assertEqual(expected_res, test_res)

    def test_load_yaml(self):
        expected_res = self.component
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.yaml") + '_test'
        test_res = self.component.load_yaml(file_name)
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_loads_yaml(self):
        expected_res = self.component
        test_res = self.component.loads_yaml(self.component.dumps_yaml(self.component))
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_dumps_json(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.json")
        with open(file_name, 'r') as file:
            expected_res = file.read()
        expected_res = expected_res.translate({ord(i): None for i in ' \t\n\r'})
        test_res = self.component.dumps_json(self.component).translate({ord(i): None for i in ' \t\n\r'})
        self.assertEqual(expected_res, test_res)

    def test_dump_json(self):
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.json")
        with open(file_name, 'r') as file:
            expected_res = file.read()
        expected_res = expected_res.translate({ord(i): None for i in ' \t\n\r'})
        test_file = file_name + '_test'
        self.component.dump_json(self.component, test_file)
        with open(test_file, 'r') as file:
            test_res = file.read().translate({ord(i): None for i in ' \t\n\r'})
        # os.remove(test_file)
        self.assertEqual(expected_res, test_res)

    def test_load_json(self):
        expected_res = self.component
        file_name = os.path.join(FIXTURES_PATH, f"{self.component.__class__.__name__}.json") + '_test'
        test_res = self.component.load_json(file_name)
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())

    def test_loads_json(self):
        expected_res = self.component
        test_res = self.component.loads_json(self.component.dumps_json(self.component))
        self.assertEqual(expected_res.__class__.__name__, test_res.__class__.__name__)
        self.assertEqual(expected_res.__dict__.keys(), test_res.__dict__.keys())


class CarTest(unittest.TestCase, BaseTestCases):
    component = Car.load_yaml(os.path.join(FIXTURES_PATH, 'Car.yaml'))
    # component = Car(car_type='SUV', producer='BENTLEY', price=43671.84, mileage=15372.55,
    #                 number='caa6be3d-0d68-4fa4-8506-9bca6d361f40')

    def test_change_number(self):
        test_car = deepcopy(self.component)
        self.assertEqual('ca9afe18-a6db-4f7b-8e3b-37e1924d8f26', test_car.number)
        test_car.change_number()
        self.assertNotEqual('ca9afe18-a6db-4f7b-8e3b-37e1924d8f26', test_car.number)


class GarageTest(unittest.TestCase, BaseTestCases):
    component = Garage.load_yaml(os.path.join(FIXTURES_PATH, 'Garage.yaml'))

    # component = Garage(town='Prague', places='5', owner='35529727-8db9-4e9d-ac39-35d675d1aa36,
    # cars='[Car(car_type='Diesel', producer='Chery', price='56646.17, mileage='98441.76',
    # number='201f8d70-ffbf-44cd-8dda-976ac6c2aae0'), Car(car_type='Diesel', producer='BMW', price='33061.71,
    # mileage='42978.05', number='6215e61a-29ac-4f90-ad47-a490722dfea2'), Car(car_type='Truck',
    # producer='Chevrolet', price='65178.62, mileage='59386.34', number='893b41d6-f822-4440-8f10-fd561867d3da'),
    # Car(car_type='Diesel', producer='BMW', price='61871.17, mileage='9503.87',
    # number='37fc05e9-2a8b-44be-8a87-9deefd0d2acf'), Car(car_type='Crossover', producer='Ford',
    # price='12504.68, mileage='84575.45', number='24841f3c-b2bb-4f77-b3c9-1542bdc816d5')]')

    def test_add(self):
        test_garage = deepcopy(self.component)
        test_car = test_garage.cars[0]
        test_garage.cars = []
        test_garage.add(test_car)
        self.assertEqual(len(test_garage.cars), 1)
        self.assertNotEqual(0, 1)

    def test_remove(self):
        test_garage = deepcopy(self.component)
        orig_len = len(test_garage.cars)
        if orig_len > 0:
            test_car = test_garage.cars[0]
            test_garage.remove(test_car)
            self.assertEqual(len(test_garage.cars) + 1, orig_len)
            self.assertNotEqual(len(test_garage.cars), 0)

    def test_hit_hat(self):
        test_garage = deepcopy(self.component)
        orig_len = len(test_garage.cars)
        orig_hit_hat = test_garage.hit_hat()
        if orig_len > 0:
            test_car = test_garage.cars[0]
            test_garage.remove(test_car)
            self.assertEqual(test_garage.hit_hat() + test_car.price, orig_hit_hat)
            self.assertNotEqual(test_garage.hit_hat(), orig_hit_hat)
        else:
            self.assertEqual(orig_hit_hat, 0)


class CesareTest(unittest.TestCase, BaseTestCases):
    component = Cesar.load_yaml(os.path.join(FIXTURES_PATH, 'Cesar.yaml'))

    def test_garages_count(self):
        self.assertEqual(self.component.garages_count(), 2)
        self.assertNotEqual(self.component.garages_count(), 0)

    def test_cars_count(self):
        test_cesare = deepcopy(self.component)
        orig_cars_count = test_cesare.cars_count()
        if orig_cars_count > 0 and len(test_cesare.garages) > 0:
            deleted_cars_count = len(test_cesare.garages[0].cars)
            del test_cesare.garages[0]
            self.assertEqual(orig_cars_count, deleted_cars_count + test_cesare.cars_count())

    def test_add_car(self):
        test_cesare = deepcopy(self.component)
        orig_cars_count = test_cesare.cars_count()
        garage_cars_count = len(test_cesare.garages[0].cars)
        if garage_cars_count > 0:
            car_to_ad = test_cesare.garages[0].cars[0]
            count_to_del = len(test_cesare.garages[0].cars)
            test_cesare.garages[0].cars = []
            test_cesare.add_car(car_to_ad)
            self.assertEqual(orig_cars_count - count_to_del + 1, test_cesare.cars_count())

    def test_hit_hat(self):
        test_cesare = deepcopy(self.component)
        if test_cesare.garages_count() > 0:
            gar_hit_hat = test_cesare.garages[0].hit_hat()
            del test_cesare.garages[0]
            self.assertEqual(test_cesare.hit_hat() + gar_hit_hat, self.component.hit_hat())
        else:
            self.assertEqual(self.component.hit_hat(), 0)


if __name__ == "__main__":
    unittest.main()
