# upgrade.py

import pygame
import time
from settings import screen_width, screen_height

class Upgrade(pygame.sprite.Sprite):
    image = pygame.image.load("upgrade_icon.png")
    image = pygame.transform.scale(image, (90, 90))

    def __init__(self, name, upgrade_type, duration=5000):  # Füge einen Standardwert für die Dauer hinzu
        super().__init__()
        self.image = Upgrade.image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.name = name
        self.type = upgrade_type
        self.duration = duration
        self.start_time = 0

    def apply_upgrade(self, player):
        if self.type == "size":
            player.size += 500000
        elif self.type == "magnet":
            player.magnet_field += 100000
        elif self.type == "multiplier":
            player.coins_multi += 2
        else:
            print(f"Warning: Unknown upgrade type '{self.type}'. Upgrade not applied.")

        existing_booster = next((upgrade for upgrade in player.upgrades if upgrade.type == self.type), None)

        if existing_booster:
            existing_booster.reset_timer()
        else:
            self.start_time = time.time()

        # Hier könnte eine Anzeige für den Spieler erfolgen (Punkt 1)
        print(f"Upgrade collected: {self.name}, Duration: {self.duration / 1000} seconds")

    def has_expired(self):
        return time.time() > self.start_time + self.duration

    def reset_timer(self):
        self.start_time = time.time()