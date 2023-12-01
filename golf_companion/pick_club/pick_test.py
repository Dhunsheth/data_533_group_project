import unittest
from start_picking import start_picking
from golf_companion import __player_class

class TestStartPickingLowYardage(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="Test Player", skill=1)  # Assuming skill level 1 has all clubs

    def test_putter_selected(self):
        self.assertEqual(start_picking(15, self.player), "Putter")

    def test_no_club_for_negative_yards(self):
        with self.assertRaises(ValueError):
            start_picking(-10, self.player)

    def test_no_club_for_zero_yards(self):
        self.assertEqual(start_picking(0, self.player), "Putter")

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            start_picking("fifty", self.player)


class TestStartPickingHighYardage(unittest.TestCase):
    def setUp(self):
        self.player = Player(name="Test Player", skill=1)  # Assuming skill level 1 has all clubs

    def test_driver_selected(self):
        self.assertEqual(start_picking(305, self.player), "Driver")

    def test_no_suitable_club_found(self):
        self.player.yardages = {club: 20 for club in self.player.yardages}  # Set all yardages to 20
        self.assertEqual(start_picking(350, self.player), "Driver")

    def test_correct_club_for_mid_range(self):
        # Assuming '5 Iron' is the club for 195 yards
        self.assertEqual(start_picking(195, self.player), "5 Iron")

    def test_type_error_for_non_number(self):
        with self.assertRaises(ValueError):
            start_picking(None, self.player)

if __name__ == '__main__':
    unittest.main()
