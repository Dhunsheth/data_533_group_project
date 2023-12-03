import sys
import pandas as pd

from golf_companion.pick_club import start_picking
from golf_companion.track_score import start_tracking
from golf_companion import __player_class


def start_game(players=[], course=None, num_holes=None):
    """
    Start a game of golf. If player or course or num_holes objects/values are passed, then the 
    user prompts for these information is skipped. If a list of player objects is passed then 
    the option to add additional/new players still remains. 

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
        List containing players, the course, and final scores.
    """
    try:
        # Prompts for course, players, and number of holes to play
        if course is None:
            course = start_tracking.__choose_course()
        if not players:
            players = start_tracking.__add_game_players()
        else:  # if players are passed then prompt to check if new players would like to be added
            for k in players:
                k.score = {}
            ask_to_add_players = None
            while ask_to_add_players is None:
                try:
                    print(f"\nPlayers in game:", end="")
                    for player in players:
                        print(f" {player.name}", end="")
                    ask_to_add_players = input("\nDo you want to add more players: \n1: Yes \n2: No\n")
                    if start_tracking.__check_value_is_number(ask_to_add_players):
                        if int(ask_to_add_players) == 1:
                            players = start_tracking.__add_game_players(players)
                        elif int(ask_to_add_players) == 2:
                            ask_to_add_players = False
                        else:
                            ask_to_add_players = None
                    else:
                        raise ValueError("Invalid input. Please enter 1 or 2.")
                except ValueError as ve:
                    print(f"Error: {ve}")
                    ask_to_add_players = None

        if num_holes is None:
            num_holes = start_tracking.__check_num_holes()

        # Starting the game tracking - will start by repeating club help prompt until no more help is required.
        # Usually players would play the full hole (i.e., may require club help) and then enter the final score once
        # the hole is complete.
        for i in range(num_holes):
            border = "-" * len(f"Hole {i + 1} | Par {course.score_card['par'][i]} | {course.score_card['yards'][i]} yards")
            print("\n" + border)
            print(f"Hole {i + 1} | Par {course.score_card['par'][i]} | {course.score_card['yards'][i]} yards")
            print(border + "\n")

            pick_club_option = None
            while pick_club_option is None:
                try:
                    pick_club_option = input("Do you need help picking a club: \n1: Yes \n2: No \n3: Exit \n")
                    print("")
                    check_pick_club_option = start_tracking.__check_value_is_number(pick_club_option)
                    if check_pick_club_option:
                        if int(pick_club_option) == 3:
                            start_tracking.__exit()
                        elif int(pick_club_option) == 1:
                            pick_club_option = None
                            which_player = None
                            while which_player is None:
                                try:
                                    print("Which player needs help picking a club?")
                                    for j in range(len(players)):
                                        print(f"{j+1}: {players[j].name}")
                                    which_player = input()
                                    check_which_player = start_tracking.__check_value_is_number(which_player)
                                    if check_which_player:
                                        if 0 < int(which_player) <= len(players):
                                            yardage = None
                                            while yardage is None:
                                                try:
                                                    yardage = input("\nEnter yardage to the flag: ")
                                                    check_yardage = start_tracking.__check_value_is_number(yardage)
                                                    if check_yardage:
                                                        if 0 < int(yardage) < 750:
                                                            club = start_picking.start_picking(int(yardage),
                                                                                                players[int(which_player) - 1])
                                                            print(f"{players[int(which_player) - 1].name} hit your {club}\n")
                                                        else:
                                                            print("Yardage should be greater than 0 and less than 750 yards.")
                                                            yardage = None
                                                    else:
                                                        which_player = None
                                                except ValueError as ve:
                                                    print(f"Error: {ve}")
                                                    yardage = None
                                        else:
                                            which_player = None
                                except ValueError as ve:
                                    print(f"Error: {ve}")
                                    which_player = None
                        elif int(pick_club_option) == 2:
                            pick_club_option = int(pick_club_option)
                        else:
                            raise ValueError("Invalid input. Please enter 1, 2, or 3.")
                    else:
                        raise ValueError("Invalid input. Please enter a number.")
                except ValueError as ve:
                    print(f"Error: {ve}")
                    pick_club_option = None

            # Tracking the final score of all players for a particular hole.
            players = start_tracking.__track_hole(players, course, i, False)

        print_summary = start_tracking.__print_summary(players, course)
        final_scores = print_summary
        min_score_index = final_scores.index(min(final_scores))
        tie = False
        for i in range(len(final_scores)):
            if final_scores[min_score_index] == final_scores[i] and i != min_score_index:
                tie = True
        if tie:
            print(f"\nThere was a tie! The following players tied for a final score of {final_scores[min_score_index]}!")
            indices = [index for index, item in enumerate(final_scores) if item == final_scores[min_score_index]]
            for i in indices:
                print(f"{players[i].name}")
        else:
            print(
                f"\nGame winner is {players[min_score_index].name} who got a final score of {final_scores[min_score_index]}!")
        print("")
        print("End of game...")
        return [players, course, final_scores]

    except Exception as e:
        print(f"Error in start_game function: {e}")
        # Optionally, you might want to log the exception for further investigation.
        # logging.exception(f"Error in start_game function: {e}")

# Example usage:
# b = start_game()
