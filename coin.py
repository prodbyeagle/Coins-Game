# coin.py
import pygame
from settings import screen_width, screen_height

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin_icon.png")  # Lade das Münzen-Icon
        self.image = pygame.transform.scale(self.image, (80, 80))  # Verkleinere das Icon
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pass