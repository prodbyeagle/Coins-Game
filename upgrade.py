# upgrade.py
import pygame
import time
from settings import screen_width, screen_height

class Upgrade(pygame.sprite.Sprite):
    image = pygame.image.load("upgrade_icon.png")
    image = pygame.transform.scale(image, (90, 90))

    def __init__(self, name, upgrade_type, duration):
        super().__init__()
        self.image = Upgrade.image.copy()  # Use a copy to avoid shared references
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

        # Check if the player already has an active booster of the same type
        existing_booster = next((upgrade for upgrade in player.upgrades if upgrade.type == self.type), None)

        # If an existing booster is found, reset its timer
        if existing_booster:
            existing_booster.reset_timer()
        else:
            # If no existing booster, set the start time for the new booster
            self.start_time = time.time()

    def has_expired(self):
        # Check if the duration has passed since the upgrade was applied
        return time.time() > self.start_time + self.duration

    def reset_timer(self):
        # Reset the start time to the current time
        self.start_time = time.time()