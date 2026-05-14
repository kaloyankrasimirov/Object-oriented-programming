from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    SPECIALIZATION = "ScientistAstronaut"
    INITIAL_STAMINA = 70

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.INITIAL_STAMINA)

    def train(self):
        self.stamina = min(100, self.stamina + 3)