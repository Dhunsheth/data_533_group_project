from golf_companion import __player_class

def start_picking(target_yards, player):
    if not isinstance(target_yards, (int, float)) or target_yards < 0:
        raise ValueError("Target yards must be a positive number.")

    # Check for special cases first
    if target_yards < 20:
        return "Putter"
    elif target_yards > 300:
        return "Driver"

    best_club = None
    min_diff = float('inf')

    for club, yardage in player.yardages.items():
        # Skip the putter and driver since we have already handled them
        if club in ["Putter", "Driver"]:
            continue

        diff = target_yards - yardage
        if 0 <= diff < min_diff:
            best_club = club
            min_diff = diff

    if best_club is None:
        return "No suitable club found."

    return best_club
