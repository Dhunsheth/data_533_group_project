import __player_class 

def start_picking(target_yards, player):
    if not isinstance(target_yards, (int, float)) or target_yards < 0:
        raise ValueError("Target yards must be a positive number.")

    best_club = None
    min_diff = float('inf')

    for club, yardage in player.yardages.items():
        diff = target_yards - yardage
        if 0 <= diff < min_diff:
            best_club = club
            min_diff = diff

    if best_club is None:
        return "No suitable club found."

    return best_club

p = __player_class .Player("Tim",2)
best_club= start_picking(200,p)
print(best_club)