from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    SPECIALIZATION = "EngineerAstronaut"
    INITIAL_STAMINA = 80

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.INITIAL_STAMINA)

    def train(self):
        self.stamina = min(100, self.stamina + 5)