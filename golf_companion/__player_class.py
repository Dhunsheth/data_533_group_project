import pandas as pd
import numpy as np

class Player:
    professional_yardages = {
    "Driver": 280,
    "3 Wood": 240,
    "5 Wood": 225,
    "4 Iron": 210,
    "5 Iron": 195,
    "6 Iron": 180,
    "7 Iron": 165,
    "8 Iron": 150,
    "9 Iron": 135,
    "Pitching Wedge": 120,
    "Sand Wedge": 21,
    "Putter": 20
    }

    def __init__(self, name, skill, handicap=None,score=None):
        self.name = name
        self.handicap = handicap
        self.skill = skill
        self.score= score
        self.yardages = self.calculate_yardages(skill)

    #Skill level 1 = pro
    def calculate_yardages (self,skill):
        beginner_multiplier = 0.6  # 60% of professional yardage
        intermediate_multiplier = 0.8  # 80% of professional yardage
        if skill == 1:
            return Player.professional_yardages
        elif skill == 2:
            return {club: int(yardage * intermediate_multiplier) for club, yardage in Player.professional_yardages.items()}
        elif skill == 3: 
            return {club: int(yardage * beginner_multiplier) for club, yardage in Player.professional_yardages.items()}

    def __str__(self):
        skill_level = "Professional" if self.skill == 1 else "Intermediate" if self.skill == 2 else "Amateur"
        output = f"\nPlayer: {self.name}\nSkill Level: {skill_level}\nHandicap: {self.handicap if self.handicap is not None else 'N/A'}\n"
        if self.score is not None:
            output += "Score:\n" + str(pd.DataFrame([self.score], index=[self.name]))
        return output

