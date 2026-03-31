from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 80
    ATTACK_COST = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

        self.ship_type = "PirateBattleship"

    def attack(self):
        self.ammunition -= self.ATTACK_COST
        if self.ammunition < 0:
            self.ammunition = 0
        return self.ammunition