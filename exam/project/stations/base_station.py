from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts:list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not all(c.isalnum() or c == "-" for c in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not value >= 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        salary_list = [a.salary for a in self.astronauts]
        total_salaries = sum(salary_list)
        return f"{total_salaries:.2f}"

    def status(self):
        middle_part = ""
        if len(self.astronauts) == 0:
            middle_part = "N/A"
        else:
            middle_part =  ' #'.join(sorted(a.id_number for a in self.astronauts))
        return f"Station name: {self.name}; Astronauts: {middle_part}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value:float):
        pass





