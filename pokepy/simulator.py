from .damage import damage_formula
from .moves import Move
from .pokemon import Pokemon
from .types import lookup_effectiveness


def simulate_move(user: Pokemon, target: Pokemon, move: Move):
    """
    user: Pokemon using `move`
    target: Pokemon on which `move` is used
    move: used by `user` against `target`
    """
    effectiveness = lookup_effectiveness(move.type1, target.type1)
    hp_lost = damage_formula(move.power, user.attack, target.defense, effectiveness)
    hp_lost = min(target.hp, hp_lost)

    target.hp -= hp_lost

    print(f"{user.name} used {move.name} against {target.name}.")
    if effectiveness > 1.0:
        print("It was super effective!")
    elif effectiveness < 1.0:
        print("It wasn't very effective...")
    print(f"{target.name} lost {hp_lost} HP!")
    if target.hp <= 0:
        print(f"{target.name} fainted!")