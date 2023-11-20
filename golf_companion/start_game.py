import sys
import pandas as pd

from golf_companion.pick_club import start_picking
from golf_companion.track_score import start_tracking
from golf_companion import __player_class

def start_game(players = [], course = None, num_holes = None):
    if course == None:
        course = start_tracking.__choose_course()
    if players == []:
        players = start_tracking.__add_game_players()
    else:
        for k in players:
            k.score = {}
        ask_to_add_players = None
        while ask_to_add_players == None:
            print(f"\nPlayers in game:", end="")
            for player in players:
                print(f" {player.name}", end="")
            ask_to_add_players = input("\nDo you want to add more players: \n1: Yes \n2: No\n")
            if start_tracking.__check_value_is_number(ask_to_add_players) == True:
                if int(ask_to_add_players) == 1:
                    players = start_tracking.__add_game_players(players)
            else:
                ask_to_add_players = None
    if num_holes == None:
        num_holes = start_tracking.__check_num_holes()
    
    for i in range(num_holes):
        border = "-" * len(f"Hole {i + 1} | Par {course.score_card['par'][i]} | {course.score_card['yards'][i]} yards")
        print("\n" + border)
        print(f"Hole {i + 1} | Par {course.score_card['par'][i]} | {course.score_card['yards'][i]} yards")
        print(border + "\n")
        pick_club_option = None
        while pick_club_option == None:
            pick_club_option = input("Do you need help picking a club: \n1: Yes \n2: No \n3: Exit \n")
            print("")
            check_pick_club_option = start_tracking.__check_value_is_number(pick_club_option)
            if check_pick_club_option == True:
                if int(pick_club_option) == 3:
                    start_tracking.__exit()
                elif int(pick_club_option) == 1:
                    pick_club_option = None
                    which_player = None
                    while which_player == None:
                        print("Which player needs help picking a club?")
                        for j in range(len(players)):
                            print(f"{j+1}: {players[j].name}")
                        which_player = input()
                        check_which_player = start_tracking.__check_value_is_number(which_player)
                        if check_which_player == True:
                            if int(which_player) > 0 and int(which_player) <= len(players):
                                yardage = None
                                while yardage == None:
                                    yardage = input("\nEnter yardage to the flag: ")
                                    check_yardage = start_tracking.__check_value_is_number(yardage)
                                    if check_yardage == True:
                                        club = start_picking.start_picking(int(yardage),players[int(which_player)-1])
                                        print(f"{players[int(which_player)-1].name} hit your {club}\n")
                                    else:
                                        which_player = None
                            else:
                                which_player = None
                elif int(pick_club_option) == 2:
                    pick_club_option = int(pick_club_option)
                else:
                    pick_club_option = None
        
        players = start_tracking.__track_hole(players, course, i, False)
    
    print_summary = start_tracking.__print_summary(players, course)
    final_scores = print_summary
    min_score_index = final_scores.index(min(final_scores))
    tie = False
    for i in range(len(final_scores)):
        if final_scores[min_score_index] == final_scores[i] and i != min_score_index:
            tie = True
    if tie == True:
        print(f"\nThere was a tie! The following players tied for a final score of {final_scores[min_score_index]}!")
        indicies = [index for index, item in enumerate(final_scores) if item == final_scores[min_score_index]]
        for i in indicies:
            print(f"{players[i].name}")
    else:
        print(f"\nGame winner is {players[min_score_index].name} who got a final score of {final_scores[min_score_index]}!")
    print("")
    print("End of game...")
    return [players, course, final_scores]
    
b = start_game()