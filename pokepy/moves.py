from dataclasses import dataclass
from .constants import POKEMON_TYPE

@dataclass
class Move:
    name: str
    type1: POKEMON_TYPE
    power: int

