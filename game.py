from dataclasses import dataclass

from hero import Hero
from sprites import Sprites, load_sprites


@dataclass
class Game:
    hero: Hero
    sprites: Sprites
    playing: bool = True

    @classmethod
    def new_game(cls, screen_10: int):
        hero = Hero(
            x=10,
            y=10,
        )
        return Game(
            hero=hero,
            sprites=load_sprites(
                hero_size=(screen_10, screen_10),
            ),
        )
