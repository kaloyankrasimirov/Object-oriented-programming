from project.soccer_player import SoccerPlayer

from unittest import TestCase, main

class SoccerPlayerTest(TestCase):
    def setUp(self):
        self.player1 = SoccerPlayer("Test Player1", 21, 350, "Barcelona")
        self.player2 = SoccerPlayer("Test Player2", 28, 286, "PSG")

    def test_init(self):
        self.assertEqual(self.player1.name, "Test Player1")
        self.assertEqual(self.player1.age, 21)
        self.assertEqual(self.player1.goals, 350)
        self.assertEqual(self.player1.team, "Barcelona")
        self.assertEqual(self.player1.achievements, {})

    def test_name_validation(self):
        with self.assertRaises(ValueError) as e:
            self.player1.name = "Test1"
        self.assertEqual("Name should be more than 5 symbols!", str(e.exception))

        with self.assertRaises(ValueError) as e2:
            self.player1.name = "Test"
        self.assertEqual("Name should be more than 5 symbols!", str(e2.exception))

    def test_age_validation(self):
        with self.assertRaises(ValueError) as e:
            self.player1.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(e.exception))

    def test_goals_validation(self):
        self.player1.goals = -1
        self.assertEqual(0, self.player1.goals)

    def test_team_validation(self):
        with self.assertRaises(ValueError) as e:
            self.player1.team = "Bayern"
        self.assertEqual(f"Team must be one of the following: "
                         "Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(e.exception))

    def test_change_team__valid_name(self):
        result = self.player1.change_team("PSG")
        self.assertEqual("PSG", self.player1.team)
        self.assertEqual("Team successfully changed!", result)

    def test_change_team__invalid_name(self):
        result = self.player1.change_team("Unknown")
        self.assertEqual("Barcelona", self.player1.team)
        self.assertEqual("Invalid team name!", result)

    def test_add_new_achievement__not_existing(self):
        result = self.player1.add_new_achievement("Test cup")
        self.assertEqual("Test cup has been successfully added to the achievements collection!", result)
        self.assertEqual(1, self.player1.achievements["Test cup"])
        self.assertEqual(1, len(self.player1.achievements))

    def test_add_new_achievement__existing(self):
        self.player1.add_new_achievement("Test cup")
        result = self.player1.add_new_achievement("Test cup")
        self.assertEqual("Test cup has been successfully added to the achievements collection!", result)
        self.assertEqual(2, self.player1.achievements["Test cup"])
        self.assertEqual(1, len(self.player1.achievements))

    def test_add_new_achievement__different(self):
        self.player1.add_new_achievement("Test cup")
        result = self.player1.add_new_achievement("Test cup 2")
        self.assertEqual("Test cup 2 has been successfully added to the achievements collection!", result)
        self.assertEqual(1, self.player1.achievements["Test cup"])
        self.assertEqual(1, self.player1.achievements["Test cup 2"])
        self.assertEqual(2, len(self.player1.achievements))

    def test_comparison(self):
        expected = self.player1 < self.player2
        self.assertEqual(expected, "Test Player1 is a better goal scorer than Test Player2.")

        expected2 = self.player2 < self.player1
        self.assertEqual(expected2, "Test Player1 is a top goal scorer! S/he scored more than Test Player2.")


if __name__ == "__main__":
    main()