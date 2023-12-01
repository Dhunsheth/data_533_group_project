# data_533_group_project
Group Project for Data-533 - Building a golf companion python package / application

**Important notes for Prof/TA**
1. *Our module structure does not follow the requirements in that each sub-package does not have 2 sub-modules because this was not necessary for our project (Khalad approved this).*
2. *From a testing perspective, we can only test certain functions where parameters can be passed, but many of our functions reply on user response/input and so are very difficult to test via a testing script and have been not included (Khalad approved this).*
3. *The testing files can be found on the "test" branch while the main code is on main.*

Instead, the golf_companion package has 2 sub-packages (track_score and pick_club) with the following modules (start_tracking.py and start_picking.py), respectively. In addition, there is another module under golf_companion called "start_game.py" that uses the 2 sub-packages to simulate a round of golf. Some modules contain class definitions and a course_files folder that stores the default courses available to play. 
*Note: there are several times when the user can choose to "Exit the program" - choosing this option will immediately end the program without storing or displaying anything further - this is similar to a forced exit*

golf_companion/  
├── __init__.py  
├── __player_class.py  
├── __course_class.py  
├── start_game.py  
│   
├── pick_club/  
│   ├── __init__.py  
│   └── start_picking.py  
│   
├── track_score/  
│   ├── __init__.py  
│   └── start_tracking.py  
│   
└── course_files/  
    ├── sunset_ranch.csv    
    ├── shadow_ridge.csv   
    └── okanagan_golf_club_bear.csv   

**start_game.py**
This module contains the main "start_game(players = [], course = None, num_holes = None)" function. If a list of player objects, course object, or number of holes to play isn't passed, the function will prompt the user to enter this information. If a list of players is passed, there is an option to add additional players to the game so it isn't like you either have to initialize or pass all game players but can do a mix as well. Once all holes have been looped through, the function will ask if the user would like to see a detailed breakdown or not - if yes then it will show the score for each player for each hole - if not then it will show the final/adjusted scores of all players and also specify which players won or tied. 

Assuming all player, course and hole information has been loaded, the function will loop through each hole, and for each hole it will:
1. Ask if help is needed to pick a club, then ask which player needs help, and then ask for the yardage before printing the club to use. This is repeated for all players until the entire hole is complete.
2. Once the entire hole has been played, the function will prompt the user to enter the final score of all players.
3. This is then repeated for the remaining holes.

**start_picking.py**
This module is used to pick a club using the "start_picking(target_yards, player)" function. It takes the target yardage you want to hit (typically the distance to the flag), and a player object to determine 
the best club to use based on the player's skill. This function is used by the start_game() function, but can also be called independently, as long as a player object has been defined. 

**start_tracking.py**
This module uses the "start_tracking(players = [], course = None, num_holes = None)" function to track the score of 1 or more players. Similar to the start_game() function, if the player or course objects aren't passed, the function will prompt the user for it. Once the player and course objects have been established, the function will loop through each hole and prompt the user to enter the final score for each player for each hole. Once all holes have been looped through, the user will have the option to either see a detailed breakdown of score by player by hole, or the total scores of all players. 

There are several helper functions in this module that are also used by the start_game() function, such as "__check_value_is_number(value)", "__exit()", "__add_new_course()", "__choose_course()", "__add_player()", "__track_hole(players, course, hole_num, print_header = True)", "__print_summary(players, course)", "__check_num_holes()", and others. 


*Note: Due to the nature of the application being a game, it heavily relies on user input, as such, the user input is checked in several instances to make sure inputs make sense. An example of this is making sure a valid number is entered, or for player names only alphabets are entered, or for entering yardage the user cannot enter more than 750 yards because a hole longer than that doesn't make sense, and finally cannot enter more than 72 holes to play because anymore doesn't make sense. This will help users detect when an inaccurate value is entered.*


