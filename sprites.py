from dataclasses import dataclass
from typing import Tuple

import pygame
from pygame import Surface


@dataclass
class Sprites:
    hero_idle_right: Surface
    hero_idle_left: Surface


def crop(big_image, rect, size):
    cropped = pygame.Surface((rect[2], rect[3]))
    cropped.blit(big_image, (0, 0), rect)
    return pygame.transform.scale(cropped, size)


def load_sprites(
        hero_size: Tuple[int, int],
) -> Sprites:

    hero_idle = pygame.image.load("img/Idle/right.png")
    hero_idle_right = pygame.transform.scale(hero_idle, hero_size)
    hero_idle_left = pygame.transform.flip(hero_idle_right, flip_x=True, flip_y=False)

    # grounds = [
    #     None,
    #     crop(jungle, (16, 224, 32, 32), brick_size),
    #     crop(jungle, (305, 209, 32, 32), brick_size),
    #     crop(jungle, (656, 136, 32, 32), brick_size),
    #     crop(jungle, (193, 241, 32, 32), brick_size),
    #     crop(jungle, (257, 241, 32, 32), brick_size)
    # ]

    return Sprites(
        hero_idle_right=hero_idle_right,
        hero_idle_left=hero_idle_left,
    )
