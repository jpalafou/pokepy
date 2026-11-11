from dataclasses import dataclass
from .constants import POKEMON_TYPE
from .stats import PokemonStats

@dataclass
class Pokemon:
    name: str
    type1: POKEMON_TYPE
    stats: PokemonStats
