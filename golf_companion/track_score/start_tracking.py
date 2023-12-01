import sys
import pandas as pd

# import __course_class
from golf_companion import __course_class
from golf_companion import __player_class

def __exit():
    """Raise SystemExit to exit the program."""
    raise SystemExit("\nExiting the program")
    sys.exit()

def __check_value_is_number(value):
    """
    Check if the input from user is a valid number.

    Parameters
    ----------
    value : str
        The input value to check.

    Returns
    -------
    bool
        True if the value is a number, False otherwise.
    """   
    try:
        int(value)
    except:
        return False
    return True

def __add_new_course():
    """
    Add a new golf course. Prompts the user for file location of the csv storing the 
    score card of the new course.

    Returns
    -------
    __course_class.Course
        A new course object.
    """
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
    """
    Choose a golf course - can also add a new course.

    Returns
    -------
    __course_class.Course or None
        The chosen course object or None if the user exits.
    """
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
    """
    Add a new player, prompts for player name, skill and handicap.

    Returns
    -------
    __player_class.Player
        A new player object.
    """
    player_name = None
    while player_name == None or player_name == "" or player_name == " " or (player_name.replace(" ", "")).isalpha() == False:
        player_name = input("\nEnter player name: \n*Note: Cannot be empty and only alphabets allowed. \n")
    
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
        player_handicap = input("\nEnter player handicap (-10 < H < 30) or press Enter to skip \n*Note: Handicap must be a number \n")
        if player_handicap != "" and player_handicap != " " and player_handicap.isnumeric() == False:
            player_handicap = None
        if __check_value_is_number(player_handicap) == True:
            if int(player_handicap) < -10 or int(player_handicap) > 30:
                player_handicap = None
    check_handicap = __check_value_is_number(player_handicap)
    if check_handicap == False:
        player_handicap = None
    else:
        player_handicap = int(player_handicap)
        
    player = __player_class.Player(player_name, int(player_skill), player_handicap)
    
    return player

def __track_hole(players, course, hole_num, print_header = True):
    """
    Track score for all players for n number of holes (hole_num).

    Parameters
    ----------
    players : list of __player_class.Player
        List of players.
    course : __course_class.Course
        Golf course object.
    hole_num : int
        Current hole number.
    print_header : bool, optional
        Whether to print the hole header. Default is True.

    Returns
    -------
    list of __player_class.Player
        Updated list of players.
    """
    if print_header == True:
        check = input("\nEnter 0 to exit, anything else will continue: ")
        if __check_value_is_number(check) == True:
            if int(check) == 0:
                __exit()
        border = "-" * len(f"\nHole {hole_num+1} | Par {course.score_card['par'][hole_num]} | {course.score_card['yards'][hole_num]} yards\n")
        print("\n" + border)
        print(f"Hole {hole_num+1} | Par {course.score_card['par'][hole_num]} | {course.score_card['yards'][hole_num]} yards")
        print(border + "\n")
    for player in players:
        if player.score == None:
            player.score = {}
        player_score = None
        while player_score == None:
            player_score = input(f"Enter the final score for {player.name}: ")
            if __check_value_is_number(player_score) == False:
                player_score = None
            else:
                player.score.update({hole_num+1: int(player_score)})
    return players

def __print_summary(players, course):
    """
    Print a summary of scores for the round. Can either print a detailed summary of scores by hole
    or print a condensed version.

    Parameters
    ----------
    players : list of __player_class.Player
        List of players.
    course : __course_class.Course
        Golf course object.

    Returns
    -------
    list
        List of final scores.
    """
    print_summary = None
    final_score = []
    total_score = []
    adjusted_score = []
    for i in range(len(players)):
        adjusted_score.append(None)
    while print_summary == None:
        print_summary = input("\nDo you wish to see a full breakdown of scores?\n1: Yes \n2: No \n3: Exit \n")
        if __check_value_is_number(print_summary) == True:
            if int(print_summary) == 3:
                __exit()
            elif int(print_summary) not in [1,2]:
                print_summary = None
    for i in range(len(players)):
        total_score.append(sum(players[i].score.values()))
        if players[i].handicap != None:
            adjusted_score[i] = sum(players[i].score.values()) - int(players[i].handicap)
    if int(print_summary) == 1:
        border = "-" * len(f"{course.course_name} | Par {course.par} | Course Record: {course.course_record}")
        print("\n" + border)
        print(f"{course.course_name} | Par {course.par} | Course Record: {course.course_record}")
        print(border)
        for i in range(len(players)):
            print(players[i])
            print(f"\nTotal Score: {total_score[i]}")
            if players[i].handicap != None:
                print(f"Adjusted Score: {adjusted_score[i]}")
    else:
        border = "-" * len(f"{course.course_name} | Par {course.par} | Course Record: {course.course_record}")
        print("\n" + border)
        print(f"{course.course_name} | Par {course.par} | Course Record: {course.course_record}")
        print(border)
        for i in range(len(players)):
            print(f"\nPlayer: {players[i].name} \nTotal Score: {total_score[i]} | Adjusted Score: {adjusted_score[i]}")
    for i in range(len(players)):
        if adjusted_score[i] == None:
            final_score.append(total_score[i])
        else:
            final_score.append(adjusted_score[i])
    return final_score

def __check_num_holes():
    """
    Check the number of holes to track.

    Returns
    -------
    int
        Number of holes.
    """
    num_holes = None
    while num_holes == None:
        num_holes = input("\nHow many holes are you going to track. Enter '0' to exit: ")
        check_num_holes = __check_value_is_number(num_holes)
        if check_num_holes == True:
            if int(num_holes) == 0:
                __exit()
            else:
                if int(num_holes) > 72 or int(num_holes) < 0:
                    print("Must track atleast 1 hole and cannot track more than 4 full games (72 holes) of golf at 1 time.")
                    num_holes = None
                else:
                    num_holes = int(num_holes)
        else:
            num_holes = None
    return num_holes

def __add_game_players(players=[]):
    """
    Add players to the game.

    Parameters
    ----------
    players : list of __player_class.Player, optional
        List of players. Default is an empty list.

    Returns
    -------
    list of __player_class.Player
        Updated list of players.
    """
    if players == []:
        players = []
    num_players = "a"
    while num_players.isnumeric() == False:
        num_players = input("\nEnter the number of players to add (max 6) or enter '0' to exit: ")
        if __check_value_is_number(num_players) == True:
            if int(num_players) == 0:
                __exit()
            elif int(num_players) > 6 or int(num_players) < 0:
                num_players = "a"
    players_already_in_game = len(players)
    for i in range(int(num_players)):
        border = "-" * len(f"Player {i+1}")
        print("\n" + border)
        print(f"Player {i + 1 + players_already_in_game}")
        print(border)
        players.append(__add_player())
    return players

def start_tracking(players = [], course = None, num_holes = None):
    """
    Track scores for a golf game.

    Parameters
    ----------
    players : list of __player_class.Player, optional
        List of players. Default is an empty list.
    course : __course_class.Course or None, optional
        Golf course object. Default is None.
    num_holes : int or None, optional
        Number of holes to track. Default is None.

    Returns
    -------
    list
        List containing players and the course.
    """
    if course == None:
        course = __choose_course()
    if course == None:
        print("No Course Choosen!")
    if players == []:
        players = __add_game_players()
    else:
        ask_to_add_players = None
        while ask_to_add_players == None:
            print(f"\nPlayers in game:", end="")
            for player in players:
                print(f" {player.name}", end="")
            ask_to_add_players = input("\nDo you want to add more players: \n1: Yes \n2: No\n")
            if __check_value_is_number(ask_to_add_players) == True:
                if int(ask_to_add_players) == 1:
                    players = __add_game_players(players)
                elif int(ask_to_add_players) == 2:
                    ask_to_add_players = False
                else:
                    ask_to_add_players = None
            else:
                ask_to_add_players = None
    if num_holes == None:
        num_holes = __check_num_holes()

    for i in range(num_holes):
        players = __track_hole(players, course, i)
    
    print_summary = __print_summary(players, course)
    
    print("\nEnd of tracking...")
    
    return [players, course]

