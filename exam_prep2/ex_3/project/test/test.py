from unittest import TestCase, main
from typing import Tuple, Optional
from project.furniture import Furniture


class TestFurniture(TestCase):
    def test_init(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60)
        )

        self.assertEqual(furniture.model, "Table")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

    def test_valid_initialization__with_passed_values(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            False,
            15.5
        )

        self.assertEqual(furniture.model, "Table")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertFalse(furniture.in_stock)
        self.assertEqual(furniture.weight, 15.5)


    def test_invalid_model__empty_string(self):
        with self.assertRaises(ValueError) as e:
            Furniture("", 199.99, (80, 120, 60))
        self.assertEqual(str(e.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as e:
            Furniture("" * 50, 199.99, (80, 120, 60))
        self.assertEqual(str(e.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_invalid_model__more_than_50(self):
        with self.assertRaises(ValueError) as e:
            Furniture("" * 51, 199.99, (80, 120, 60))
        self.assertEqual(str(e.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_price__less_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Furniture("Table", -1, (80, 120, 60))
        self.assertEqual(str(e.exception), "Price must be a non-negative number.")

    def test_dimensions__less_than_3_integers(self):
        with self.assertRaises(ValueError) as e:
            Furniture("Table", 199.99, (80, 120))
        self.assertEqual(str(e.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions__more_than_3_integers(self):
        with self.assertRaises(ValueError) as e:
            Furniture("Table", 199.99, (80, 120, 60, 20))
        self.assertEqual(str(e.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions__tuple_integers_greater_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Furniture("Table", 199.99, (80, 120, -1))
        self.assertEqual(str(e.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_dimensions__tuple_integers_eq_to_zero(self):
        with self.assertRaises(ValueError) as e:
            Furniture("Table", 199.99, (80, 0, 60))
        self.assertEqual(str(e.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_weight__greater_than_zero(self):
        with self.assertRaises(ValueError) as e:
            furniture = Furniture(
                "Table",
                199.99,
                (80, 120, 60),
                False,
                0
            )
        self.assertEqual(str(e.exception), "Weight must be greater than zero.")

        with self.assertRaises(ValueError) as e:
            furniture = Furniture(
                "Table",
                199.99,
                (80, 120, 60),
                False,
                -1

            )
        self.assertEqual(str(e.exception), "Weight must be greater than zero.")


    def test_valid_get_available_status(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,
        )

        self.assertEqual(furniture.get_available_status(), "Model: Table is currently in stock.")

    def test_valid_get_available_status__unavailable(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            False,
        )

        self.assertEqual(furniture.get_available_status(), "Model: Table is currently unavailable.")

    def test_get_specifications__with_weight(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,
            15.5
        )

        self.assertEqual(furniture.get_specifications(), "Model: Table has the following dimensions: "
                                                         "80mm x 120mm x 60mm and weighs: 15.5")

    def test_get_specifications__without_weight(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,

        )

        self.assertEqual(furniture.get_specifications(), "Model: Table has the following dimensions: "
                                                         "80mm x 120mm x 60mm and weighs: N/A")

if __name__ == "__main__":
    main( )