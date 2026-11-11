

def compute_damage(power: int, attack: int, defense: int) -> int:
    """
    power: move-specific stat
    attack: stat of pokemon using the move
    defense: stat of pokemon on which the move is used

    returns: damage (# of HP units subtracted from target)
    """
    return 22 * power * attack / defense / 50 + 2