import pandas as pd
import os

class Course:
    def __init__(self, course_name, file_path, course_record=None):
        self.course_name = course_name
        try:
            score_card = pd.read_csv(file_path)
        except:
            raise ValueError("Error with file or file path, please try again.")
        self.score_card = score_card
        self.course_record = course_record
        try:
            par = sum(self.score_card['par'])
        except:
            raise ValueError("Could not read course par values, make sure they are integers")
        self.par = int(par)
        
    def add_course(course_name, file_path, course_record=None):
        try:
            pd.read_csv(file_path)
        except:
            return "ERROR"
        return Course(course_name, file_path, course_record)
    
    def __str__(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        return f"\nCourse: {self.course_name} \nCourse Record: {self.course_record}\nPar: {self.par} \nScore Card:\n{self.score_card.T}\n"

script_dir = os.path.dirname(os.path.abspath(__file__)) + "\\course_files"

sunset_ranch_course_record = 65
csv_file_path = os.path.join(script_dir, "sunset_ranch.csv")
sunset_ranch_course = Course("Sunset Ranch",csv_file_path, sunset_ranch_course_record)

shadow_ridge_course_record = 64
csv_file_path = os.path.join(script_dir, "shadow_ridge.csv")
shadow_ridge_course = Course("Shadow Ridge", csv_file_path, shadow_ridge_course_record)

okanagan_golf_club_bear_course_record = 68
csv_file_path = os.path.join(script_dir, "okanagan_golf_club_bear.csv")
okanagan_golf_club_bear_course = Course("Okanagan Golf Club Bear",csv_file_path, okanagan_golf_club_bear_course_record)

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')