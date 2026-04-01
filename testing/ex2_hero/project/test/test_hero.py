from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "TestUsername"
    level = 20
    health = 100.0
    damage = 50.2

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attributes(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_same_user_name_exception(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_health_less_than_zero(self):
        self.hero.health = -1
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_health_eq_zero(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as e2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e2.exception))


    def test_enemy_health_less_than_zero(self):
        enemy = Hero("Enemy", 20, -1, 15)
        with self.assertRaises(ValueError) as e3:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e3.exception))

    def test_enemy_health_eq_zero(self):
        enemy = Hero("Enemy", 20, 0, 15)
        with self.assertRaises(ValueError) as e4:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e4.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-904.0, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_victory(self):
        enemy = Hero("Enemy", 5, 20, 2)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(21, self.hero.level)
        self.assertEqual(95.0, self.hero.health)
        self.assertEqual(55.2, self.hero.damage)

    def test_enemy_victory(self):
        enemy = Hero("Enemy", 50, 1001, 200)
        self.hero.damage = 1
        self.hero.health = 30
        self.hero.level = 5

        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(51, enemy.level)
        self.assertEqual(1001, enemy.health)
        self.assertEqual(205, enemy.damage)

    def test_str(self):
        expected = (f"Hero {self.hero.username}: {self.hero.level} lvl\n" 
                  f"Health: {self.hero.health}\n" 
                  f"Damage: {self.hero.damage}\n")
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == "__main_":
    main()