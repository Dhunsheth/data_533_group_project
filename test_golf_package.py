import sys
import os

#### Used to append the package path to your system path in the event the 
#### golf_companion module can't be found.
# # Specify the folder name or path
# folder_name = 'golf_companion'

# # Get the current working directory
# current_directory = os.getcwd()

# # Join the current directory with the folder name
# folder_path = os.path.join(current_directory, folder_name)
# sys.path.append(folder_path)

from golf_companion import start_game
from golf_companion import track_score
from golf_companion import pick_club

"""
start_game(players = [], course = None, num_holes = None) funtion:

This is the main function of the package that simulates a game of golf. 
Calling this function without any arguments will prompt the user to create
the neccessary player objects, choose a course, and specify the number of
holes to play. If any of these arguments are passed, then the prompting of this
information will be skipped. 

Once these objects are ready, the round of golf will commence and each hole
will be played, starting with a loop to pick a club until no player requires
any more help. Then the final scores of each player will be entered for the
first hole. The process of picking a club and entering the final score will
be repeated until all holes are complete. 

At the end, the user will be prompted to either print a detailed summary or
a condensed version and state which players won or tied. 

*Note: if the exit option is chosen at any point then the progrom will end
without saving or displaying any information - similar to a force quit.

Returns [players, course, final_scores] where players is the list of player 
objects, course is the course object, and final_scores is a list of the final
scores of the players - this only captures their final score (if no handicap)
or the adjusted final score is the player had a handicap specified. 
"""
golf_game = start_game.start_game()
## To run after the first instance of start_game() is run and you want to skip player/course selection.
# golf_game = golf_companion.start_game.start_game(golf_game[0], golf_game[1])

"""
start_tracking(players = [], course = None, num_holes = None) function:
    
This function is to call the score tracking functionality only. Similar to 
start_game(), if the list of player objects, or course, or number of holes 
isn't passed to the function, it will prompt the use to enter this information.

Each hole will be looped through, the option to pick club is not included here
as its only for tracking score - user will input the final score of all players
and continue to the next hole. 

Once all holes have been looped through, the user can either print a detailed
verion of the score summary where it prints the score of each player by hole
or a condensed version which only shows the totals. 

Returns [players, course] where players is the list of player objects and the
course object. 
"""
score = track_score.start_tracking.start_tracking()
## To run after the first instance of start_tracking() has been run and the 
## player/course objects have been created. 
# score = track_score.start_tracking.start_tracking(score[0], score[1])

"""
start_picking(target_yardage, player) function:
    
The start_picking() function is used to determine what club to hit for a target
yardage. This function requires a target yardage and a single player object 
to be passed.

Returns the club to hit.
"""
club_1 = pick_club.start_picking.start_picking(200, golf_game[0][0])
print(club_1)
club_2 = pick_club.start_picking.start_picking(125, golf_game[0][0])
club_3 = pick_club.start_picking.start_picking(10, golf_game[0][0])
print(club_3)