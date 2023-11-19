import sys
import pandas as pd

import __course_class
from golf_companion import __player_class

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
        player_name = input("\nEnter player name: \n*Note: Cannot be empty \n")
    
    player_skill = None
    while player_skill == None or player_skill == "" or player_skill == " ":
        player_skill = input("\nChoose player skill. \nEnter: \n1: Professional \n2: Intermediate \n3: Amateur \n0: Exit \n")
        if __check_value_is_number(player_skill) == True:
            if int(player_skill) not in [0,1,2,3]:
                player_skill = None
            elif int(player_skill) == 0:
                __exit()                
        else:
            player_skill = None
    
    player_handicap = None
    while player_handicap == None:
        player_handicap = input("\nEnter player handicap or press Enter to skip \n*Note: Handicap must be a number \n")
        if player_handicap != "" and player_handicap != " " and player_handicap.isnumeric() == False:
            player_handicap = None
    
    check_handicap = __check_value_is_number(player_handicap)
    if check_handicap == False:
        player_handicap = None
    else:
        player_handicap = int(player_handicap)
        
    player = __player_class.Player(player_name, int(player_skill), player_handicap)
    
    return player

def __start_tracking(players, course, num_holes):
    for i in range(num_holes):
        check = input("Enter 0 to exit, anything else will continue: ")
        if __check_value_is_number(check) == True:
            if int(check) == 0:
                __exit()
        print(f"\nHole {i+1} | Par {course.score_card['par'][i]} | {course.score_card['yards'][i]} yards\n")
        for player in players:
            if player.score == None:
                player.score = {}
            player_score = None
            while player_score == None:
                player_score = input(f"\nEnter the final score for {player.name}: ")
                if __check_value_is_number(player_score) == False:
                    player_score = None
                else:
                    player.score.update({(i+1):int(player_score)})
                    
    return players

def __print_summary(players, course):
    print_summary = None
    while print_summary == None:
        print_summary = input("\nDo you wish to see the final scores?\n1: Yes \n2: No \n3: Exit \n")
        if __check_value_is_number(print_summary) == True:
            if int(print_summary) == 3:
                __exit()
            elif int(print_summary) not in [1,2]:
                print_summary = None
    if int(print_summary) == 1:
        print(f"\n{course.course_name} | Par {course.par} | Course Record: {course.course_record}")
        for player in players:
            print(player)
            print(f"\nTotal Score: {sum(player.score.values())}")
            if player.handicap != None:
                print(f"Adjusted Score: {sum(player.score.values()) - int(player.handicap)}")
    return

def track_score(players = [], course = None, num_holes = None):
    if course == None:
        course = __choose_course()
    if course == None:
        print("No Course Choosen!")
    if players == []:
        num_players = "a"
        while num_players.isnumeric() == False:
            num_players = input("\nEnter the number of players or enter '0' to exit: ")
            if __check_value_is_number(num_players) == True:
                if int(num_players) == 0:
                    __exit()
        for i in range(int(num_players)):
            print(f"\nPlayer {i+1}")
            players.append(__add_player())
    else:
        num_players = len(players)
    
    while num_holes == None:
        num_holes = input("\nHow many holes are you going to track. Enter '0' to exit: ")
        check_num_holes = __check_value_is_number(num_holes)
        if check_num_holes == True:
            if int(num_holes) == 0:
                __exit()
            else:
                num_holes = int(num_holes)
        else:
            num_holes = None
    
    players = __start_tracking(players, course, num_holes)
    
    print_summary = __print_summary(players, course)
    
    print("\nEnd of tracking...")
    
    return [players, course]

b = track_score()
#for i in b[1]:
#    print(i)
