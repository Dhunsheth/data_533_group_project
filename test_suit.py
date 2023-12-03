import unittest
import golf_companion
from golf_companion import player_test
from golf_companion import test_course
from golf_companion import track_score
from golf_companion.pick_club import pick_test


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(player_test.TestPlayerProfessional('test_name'))
    suite.addTest(player_test.TestPlayerProfessional('test_skill'))
    suite.addTest(player_test.TestPlayerProfessional('test_yardages'))
    suite.addTest(player_test.TestPlayerProfessional('test_handicap'))
    
    suite.addTest(player_test.TestPlayerAmateur('test_name'))
    suite.addTest(player_test.TestPlayerAmateur('test_skill'))
    suite.addTest(player_test.TestPlayerAmateur('test_yardages'))
    suite.addTest(player_test.TestPlayerAmateur('test_handicap'))  
    
    suite.addTest(test_course.TestCourseOkanagan('test_course_name'))
    suite.addTest(test_course.TestCourseOkanagan('test_course_record'))
    suite.addTest(test_course.TestCourseOkanagan('test_course_par'))
    suite.addTest(test_course.TestCourseOkanagan('test_course_score_card_type'))
    
    suite.addTest(test_course.TestCourseShadowRidge('test_course_name'))
    suite.addTest(test_course.TestCourseShadowRidge('test_course_record'))
    suite.addTest(test_course.TestCourseShadowRidge('test_course_par'))
    suite.addTest(test_course.TestCourseShadowRidge('test_course_score_card_type'))   
    
    suite.addTest(pick_test.TestStartPickingLowYardage('test_putter_selected'))
    suite.addTest(pick_test.TestStartPickingLowYardage('test_no_club_for_negative_yards'))
    suite.addTest(pick_test.TestStartPickingLowYardage('test_no_club_for_zero_yards'))
    suite.addTest(pick_test.TestStartPickingLowYardage('test_invalid_input_type'))
    
    suite.addTest(pick_test.TestStartPickingHighYardage('test_driver_selected'))
    suite.addTest(pick_test.TestStartPickingHighYardage('test_no_suitable_club_found'))
    suite.addTest(pick_test.TestStartPickingHighYardage('test_correct_club_for_mid_range'))
    suite.addTest(pick_test.TestStartPickingHighYardage('test_type_error_for_non_number'))
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()