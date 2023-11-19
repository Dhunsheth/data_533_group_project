import sys
import pandas as pd
import __course_class


def __exit():
    raise SystemExit("\nExiting the program")
    sys.exit()

def __check_value_is_number(value):
    try:
        int(value)
    except:
        return False
    return True

def __add_new_course():
    file_path = None
    while file_path == None:
        file_path = input("\nEnter file path to course score card: \n\n*Note: File must be csv and have the column headings 'hole' | 'yards' | 'par' - in that order.\n\nPress 5 if you want to exit. \n")
        
        check_file_path = __check_value_is_number(file_path)
        if check_file_path == True and int(file_path) == 5:
            __exit()
        
        try:
            pd.read_csv(file_path)
        except:
            file_path = None
            print("\nCould not find or read file, try again. \n")
        if file_path != None:
            course_name = input("\nEnter a name for the course: ")
            course_record = input("\nEnter the course record, if you know it, or enter 0: \n*Note: Any value other than 0 or a valid integer will not be used.\n")
    
    if course_name == "" or course_name == " ":
        course_name = None
    check_course_record = __check_value_is_number(course_record)
    
    if not course_record.isnumeric() or int(course_record) == 0:
        course_record = None   
    new_course = __course_class.Course.add_course(course_name, file_path, course_record)
    
    return new_course

def __choose_course():
    course = None
    while course == None:
        course = input("\nWhat course would you like to play? \nPress: \n1: Sunset Ranch \n2: Shadow Ridge \n3: Okanagan Golf Club Bear \n4: Load Your own course\n5: Exit \n")
        check_course = __check_value_is_number(course)
        if check_course == True:
            course = int(course)
        else:
            course = None
        if course not in [1,2,3,4,5]:
                print("\nPlease choose one of the listed options")
                course = None
    if course == 5:
        __exit()
    elif course == 1:
        return __course_class.sunset_ranch_course
    elif course == 2:
        return __course_class.shadow_ridge_course
    elif course == 3:
        return __course_class.okanagan_golf_club_bear_course
    elif course == 4:
        return __add_new_course()
    return None

def __add_player():
    player_name = None
    while player_name == None or player_name == "" or player_name == " ":
        player_name = input("\nEnter player name: \n*Note: Cannot be empty\n ")
    
    player_skill = None
    while player_skill == None or player_skill == "" or player_skill == " ":
        player_skill = input("\nChoose player skill. \nEnter: \n1: Professional \n2: Intermediate \n3: Amateur \n0: Exit")
        if __check_value_is_number(player_skill) == True:
            if int(player_skill) not in [0,1,2,3]:
                player_skill = None
            elif int(player_skill) == 0:
                __exit()                
        else:
            player_skill = None
    player = Player
    
    
def track_score(players=None, course=None):
    if course == None:
        course = __choose_course()
    if course == None:
        print("No Course Choosen!")
    
    
    if players = None:
        num_players = "a"
        while num_players == False:
            num_players = input("\nEnter the number of players or enter '0' to exit: ")
            if __check_value_is_number(num_players) == True:
                if int(num_players) == 0:
                    __exit()
        for i in range(int(num_players)):
            players.append(__add_player())
    else:
        num_players = len(players)
    
    return course

