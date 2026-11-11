from dataclasses import dataclass
from .constants import POKEMON_TYPE

@dataclass
class Pokemon:
    name: str
    type1: POKEMON_TYPE
    hp: int
    attack: int
    defense: int
