from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof-woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"



def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat()]
animal_sound(animals)