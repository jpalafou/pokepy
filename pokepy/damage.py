

def damage_formula(power: int, attack: int, defense: int, effectiveness: float) -> int:
    """
    power: move-specific stat
    attack: stat of pokemon using the move
    defense: stat of pokemon on which the move is used
    effectiveness: damage multiplier

    returns: damage (# of HP units subtracted from target)
    """
    out = 22 * power * attack / defense / 50 + 2
    out *= effectiveness
    return int(out)
