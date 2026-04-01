from project.mammal import Mammal
from unittest import TestCase, main

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Oscar",
                             "cat",
                             "meow")



    def test_init(self):
        self.assertEqual("Oscar", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_sound(self):
        actual = self.mammal.make_sound()
        self.assertEqual("Oscar makes meow", actual)

    def test_kingdom(self):
        actual = self.mammal.get_kingdom()
        self.assertEqual("animals", actual)

    def test_info(self):
        actual = self.mammal.info()
        self.assertEqual("Oscar is of type cat", actual)

if __name__ == "__main__":
    main()