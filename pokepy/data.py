from dataclasses import dataclass
from .constants import POKEMON_TYPE
from .stats import PokemonStats

@dataclass
class PokemonData:
    level: int
    type1: POKEMON_TYPE
    stats: PokemonStats
