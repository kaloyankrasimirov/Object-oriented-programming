from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 36.5
    horse_power = 135.8
    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(30.25, self.vehicle.fuel)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1.5)
        self.assertEqual(2.5, self.vehicle.fuel)

    def test_refuel_fail(self):
        self.vehicle.fuel = 30
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(15.7)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        actual = self.vehicle.__str__()
        self.assertEqual("The vehicle has 135.8 "
                         "horse power with 36.5 fuel left "
                         "and 1.25 fuel consumption", actual)



if __name__ == "__main__":
    main()