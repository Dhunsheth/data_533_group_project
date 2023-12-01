from __course_class import Course # delte this 
# from golf_companion import __course_class
import unittest
import os
import pandas as pd


class TestCourseOkanagan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        cls.csv_file_path = os.path.join(current_directory, "course_files", "okanagan_golf_club_bear.csv")

    def setUp(self):
        self.course = Course("Okanagan Golf Club Bear", TestCourseOkanagan.csv_file_path, 68)

    def test_course_name(self):
        self.assertEqual(self.course.course_name, "Okanagan Golf Club Bear")

    def test_course_record(self):
        self.assertEqual(self.course.course_record, 68)

    def test_course_par(self):
        expected_par = self.course.score_card['par'].sum()
        self.assertEqual(self.course.par, expected_par)

    def test_course_score_card_type(self):
        self.assertIsInstance(self.course.score_card, pd.DataFrame)


class TestCourseShadowRidge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        cls.csv_file_path = os.path.join(current_directory, "course_files", "okanagan_golf_club_bear.csv")

    def setUp(self):
        self.course = Course("Shadow Ridge", TestCourseShadowRidge.csv_file_path, 64)

    def test_course_name(self):
        self.assertEqual(self.course.course_name, "Shadow Ridge")

    def test_course_record(self):
        self.assertEqual(self.course.course_record, 64)

    def test_course_par(self):
        expected_par = self.course.score_card['par'].sum()
        self.assertEqual(self.course.par, expected_par)

    def test_course_score_card_type(self):
        self.assertIsInstance(self.course.score_card, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
