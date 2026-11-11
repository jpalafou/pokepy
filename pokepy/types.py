from .constants import POKEMON_TYPE

def _grass_effectiveness(defender: POKEMON_TYPE):
    match defender:
        case "grass":
            return 0.5
        case "fire":
            return 0.5
        case "water":
            return 2.0
    return 1.0

def _fire_effectiveness(defender: POKEMON_TYPE):
    match defender:
        case "grass":
            return 2.0
        case "fire":
            return 0.5
        case "water":
            return 0.5
    return 1.0

def _water_effectiveness(defender: POKEMON_TYPE):
    match defender:
        case "grass":
            return 0.5
        case "fire":
            return 2.0
        case "water":
            return 0.5
    return 1.0

def type_effectiveness(attacker: POKEMON_TYPE, defender: POKEMON_TYPE) -> float:
    match attacker:
        case "grass":
            return _grass_effectiveness(defender)
        case "fire":
            return _fire_effectiveness(defender)
        case "water":
            return _water_effectiveness(defender)
    return 1.0
                