from dataclasses import dataclass


@dataclass(order=True)
class Country:
     name: str
     population: int
     continent: str
     official_lang: str

smallestAfrica= Country("Gambia", 2521126, "Africa", "English")