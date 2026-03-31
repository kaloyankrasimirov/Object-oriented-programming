from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    ATTACK_COST = 25

    def __init__(self,name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

        self.ship_type = "RoyalBattleship"

    def attack(self):
        self.ammunition -= self.ATTACK_COST
        if self.ammunition < 0:
            self.ammunition = 0
        return self.ammunition

