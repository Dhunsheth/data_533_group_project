import unittest
## from golf_companion import _player_class
from __player_class import Player # delete this

class TestPlayerProfessional(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup for TestPlayerProfessional')

    @classmethod
    def tearDownClass(cls):
        print('Teardown for TestPlayerProfessional')

    def setUp(self):
        self.player = Player(name="John Doe", skill=1)  # Professional skill level

    def tearDown(self):
        self.player = None

    def test_name(self):
        self.assertEqual(self.player.name, "John Doe")

    def test_skill(self):
        self.assertEqual(self.player.skill, 1)

    def test_yardages(self):
        self.assertEqual(self.player.yardages, Player.professional_yardages)

    def test_handicap(self):
        self.assertIsNone(self.player.handicap)


class TestPlayerAmateur(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup for TestPlayerAmateur')

    @classmethod
    def tearDownClass(cls):
        print('Teardown for TestPlayerAmateur')

    def setUp(self):
        self.player = Player(name="Jane Doe", skill=3)  # Amateur skill level

    def tearDown(self):
        self.player = None

    def test_name(self):
        self.assertEqual(self.player.name, "Jane Doe")

    def test_skill(self):
        self.assertEqual(self.player.skill, 3)

    def test_yardages(self):
        amateur_yardages = {club: int(yardage * 0.6) for club, yardage in Player.professional_yardages.items()}
        self.assertEqual(self.player.yardages, amateur_yardages)

    def test_handicap(self):
        self.assertIsNone(self.player.handicap)


if __name__ == '__main__':
    unittest.main()
