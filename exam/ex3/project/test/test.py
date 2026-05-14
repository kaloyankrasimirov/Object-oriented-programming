from unittest import TestCase, main

from ex3.project.star_system import StarSystem


class TestStarSystem(TestCase):
    def setUp(self):
        self.system = StarSystem("Alpha Centauri", "Yellow dwarf", "Single", 4, (0.8, 1.5))

    def test_correct_initialization(self):
        self.assertEqual(self.system.name, "Alpha Centauri")
        self.assertEqual(self.system.star_type, "Yellow dwarf")
        self.assertEqual(self.system.system_type, "Single")
        self.assertEqual(self.system.num_planets, 4)
        self.assertEqual(self.system.habitable_zone_range, (0.8, 1.5))

    def test_is_habitable_true(self):
        self.assertTrue(self.system.is_habitable)

    def test_is_habitable_false_no_planets(self):
        self.system.num_planets = 0
        self.assertFalse(self.system.is_habitable)

    def test_is_habitable_false_no_zone(self):
        self.system.habitable_zone_range = None
        self.assertFalse(self.system.is_habitable)

    def test_greater_than_comparison(self):
        system2 = StarSystem("Vega", "Blue giant", "Single", 2, (1.0, 1.5))

        self.assertTrue(self.system > system2)
        self.assertFalse(system2 > self.system)

    def test_greater_than_raises_error_if_not_habitable(self):
        system2 = StarSystem("Vega", "Blue giant", "Single", 0, None)

        with self.assertRaises(ValueError) as ve:
            result = self.system > system2
        self.assertEqual(str(ve.exception),
                         "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_compare_star_systems_wider_zone(self):
        system2 = StarSystem("Vega", "Blue giant", "Single", 2, (1.0, 1.5))

        expected = "Alpha Centauri has a wider habitable zone than Vega."
        result = StarSystem.compare_star_systems(self.system, system2)
        self.assertEqual(result, expected)

    def test_compare_star_systems_equal_zones(self):
        system2 = StarSystem("Beta Centauri", "Yellow dwarf", "Single", 4, (0.8, 1.5))
        result = StarSystem.compare_star_systems(self.system, system2)
        self.assertIn("equal", result.lower())

    def test_compare_star_systems_error_handling(self):
        system2 = StarSystem("Vega", "Blue giant", "Single", 0, None)

        expected = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        result = StarSystem.compare_star_systems(self.system, system2)
        self.assertEqual(result, expected)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.system.name = "   "
        self.assertEqual(str(ve.exception), "Name must be a non-empty string.")

    def test_invalid_star_type_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.system.star_type = "Supergiant"
        self.assertIn("Star type must be one of", str(ve.exception))

    def test_invalid_system_type_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.system.system_type = "Septuple"
        self.assertIn("System type must be one of", str(ve.exception))

    def test_negative_planets_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.system.num_planets = -1
        self.assertEqual(str(ve.exception), "Number of planets must be a non-negative integer.")

    def test_invalid_habitable_zone_range_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.system.habitable_zone_range = (0.5,)
        self.assertEqual(str(ve.exception),
                         "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

        with self.assertRaises(ValueError) as ve:
            self.system.habitable_zone_range = (1.5, 0.8)
        self.assertEqual(str(ve.exception),
                         "Habitable zone range must be a tuple of two numbers (start, end) where start < end.")

if __name__ == "__main__":
    main()