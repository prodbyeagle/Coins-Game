# upgrade.py
import pygame
from settings import screen_width, screen_height

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, name, upgrade_type, duration):
        super().__init__()
        self.image = pygame.image.load("upgrade_icon.png")  # Lade das Upgrade-Icon
        self.image = pygame.transform.scale(self.image, (90, 90))  # Verkleinere das Icon
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.name = name
        self.type = upgrade_type
        self.duration = duration

    def apply_upgrade(self, player):
        if self.type == "speed":
            player.speed += 2
        elif self.type == "size":
            player.size += 5
        elif self.type == "magnet":
            player.magnet_field += 1
        elif self.type == "multiplier":
            player.coins_multi += 1

    def update(self):
        pass